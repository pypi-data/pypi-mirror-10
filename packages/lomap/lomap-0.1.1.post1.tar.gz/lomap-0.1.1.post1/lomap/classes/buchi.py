# Copyright (C) 2012-2015, Alphan Ulusoy (alphan@bu.edu)
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import networkx as nx
import re
import subprocess as sp
import itertools as it
from model import Model
from . import ltl2ba_binary
import logging

# Logger configuration
logger = logging.getLogger(__name__)
#logger.addHandler(logging.NullHandler())

class Buchi(Model):
	"""
	Base class for non-deterministic Buchi automata.
	"""

	def buchi_from_formula(self, formula):

		##
		# Execute ltl2ba and get output
		##
		try:
			lines = sp.check_output([ltl2ba_binary, '-f', '"%s"' % formula]).splitlines()
		except Exception as ex:
			raise Exception(__name__, "Problem running ltl2ba: '%s'" % ex)

		lines = map(lambda x: x.strip(), lines)

		##
		# Get the set of propositions
		##

		# Replace operators [], <>, X, !, (, ), &&, ||, U, ->, <-> G, F, X, R, V
		# with white-space
		props = re.sub(r'[\[\]<>X!\(\)\-&|UGFRV]', ' ', formula)
		# Replace true and false with white space
		props = re.sub(r'\btrue\b', ' ', props)
		props = re.sub(r'\bfalse\b', ' ', props)
		# What remains are propositions seperated by whitespaces
		props = set(props.strip().split())

		# Form the bitmap dictionary of each proposition
		# Note: range goes upto rhs-1
		self.props = dict(zip(props, map(lambda x: 2 ** x, range(0, len(props)))))

		# Alphabet is the power set of propositions, where each element
		# is a symbol that corresponds to a tuple of propositions
		# Note: range goes upto rhs-1
		self.alphabet = set(range(0, 2 ** len(self.props)))

		# Remove 'never' first line and '}' last line
		del lines[0]
		del lines[-1]

		# remove 'if', 'fi;' lines
		lines = filter(lambda x: x != 'if' and x != 'fi;', lines)

		# '::.*' means transition, '.*:' means state
		# print '\n'.join(lines)
		# print "\n"
		this_state = None
		for line in lines:
			if(line[0:2] == '::'):
				m = re.search(':: (.*) -> goto (.*)', line)
				guard = m.group(1)
				bitmaps = self.get_guard_bitmap(guard)
				next_state = m.group(2)
				# Add edge
				self.g.add_edge(this_state, next_state, None, {'weight': 0, 'input': bitmaps, 'guard' : guard, 'label': guard})
			elif line[0:4] == 'skip':
				# Add self-looping edge
				self.g.add_edge(this_state, this_state, None, {'weight': 0, 'input': self.alphabet, 'guard' : '(1)', 'label': '(1)'})
			else:
				this_state = line[0:-1]
				# Add state
				self.g.add_node(this_state)
				# Mark final or init
				if(this_state.endswith('init')):
					self.init[this_state] = 1
				if(this_state.startswith('accept')):
					self.final.add(this_state)

	def get_guard_bitmap(self, guard):

		# Get sets for all props
		for key in self.props:
			guard = re.sub(r'\b%s\b' % key, "self.symbols_w_prop('%s')" % key, guard)

		# Handle (1)
		guard = re.sub(r'\(1\)', 'self.alphabet', guard)

		# Handler negated sets
		guard = re.sub('!self.symbols_w_prop', 'self.symbols_wo_prop', guard)

		# Convert logic connectives
		guard = re.sub(r'\&\&', '&', guard)
		guard = re.sub(r'\|\|', '|', guard)

		exec("bitmaps = %s" % guard)
		return bitmaps

	def symbols_w_prop(self, prop):
		return set(filter(lambda symbol: True if self.props[prop] & symbol else False, self.alphabet))

	def symbols_wo_prop(self, prop):
		return self.alphabet.difference(self.symbols_w_prop(prop))

	def bitmap_of_props(self, props):
		prop_bitmap = reduce(lambda x, y: x | y, map(lambda p: self.props.get(p, 0), props), 0)
		return prop_bitmap

	def next_states_of_buchi(self, q, props):
		# Get the bitmap representation of props
		prop_bitmap = self.bitmap_of_props(props)

		# Return an array of next states
		return filter(lambda x: True if x is not None else False,
							# next state if bitmap is in inputs else None
							map(lambda e: e[1] if prop_bitmap in e[2]['input'] else None,
							# Get all edges from q
							self.g.out_edges_iter(q,True)))

	def determinize(self):
		# Pg. 157 of Baier's book
		# Powerset construction

		# The new deterministic automaton
		det = Buchi()

		# List of state sets
		state_map = []

		# New initial state
		state_map.append(set(self.init.keys()))
		det.init[0] = 1

		# Copy the old alphabet
		det.alphabet = set([a for a in self.alphabet])

		# Copy the old props
		det.props = dict()
		for k,v in self.props.iteritems():
			det.props[k] = v

		# Discover states and transitions
		stack = [0]
		done = set()
		while stack:
			cur_state_i = stack.pop()
			cur_state_set = state_map[cur_state_i]
			next_states = dict()
			for cur_state in cur_state_set:
				for _,next_state,data in self.g.out_edges_iter(cur_state, True):
					inp = iter(data['input']).next()
					if inp not in next_states:
						next_states[inp] = set()
					next_states[inp].add(next_state)

			for inp,next_state_set in next_states.iteritems():
				if next_state_set not in state_map:
					state_map.append(next_state_set)
				next_state_i = state_map.index(next_state_set)
				det.g.add_edge(cur_state_i,next_state_i,attr_dict={'weight':0,'label':inp,'input':set([inp])})
				if next_state_i not in done:
					stack.append(next_state_i)
					done.add(next_state_i)

		# Sanity check
		# All edges of all states must be deterministic
		for state in det.g:
			ins = set()
			for u,v,d in det.g.out_edges_iter(state,True):
				assert len(d['input']) == 1
				inp = iter(d['input']).next()
				if inp in ins:
					assert False
				ins.add(inp)

		# Mark final states
		for state_i,state_set in enumerate(state_map):
			if state_set & self.final:
				det.final.add(state_i)

		return det
