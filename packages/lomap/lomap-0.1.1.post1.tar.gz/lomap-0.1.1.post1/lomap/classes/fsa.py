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
from . import scheck_binary
import logging

# Logger configuration
logger = logging.getLogger(__name__)
#logger.addHandler(logging.NullHandler())

class Fsa(Model):
	"""
	Base class for deterministic finite state automata.
	"""


	@staticmethod
	def infix_formula_to_prefix(formula):
		# This function expects a string where operators and parantheses 
		# are seperated by single spaces, props are lower-case.
		#
		# Tokenizes and reverses the input string.
		# Then, applies the infix to postfix algorithm.
		# Finally, reverses the output string to obtain the prefix string.
		#
		# Infix to postfix algorithm is taken from:
		# http://www.cs.nyu.edu/courses/fall09/V22.0102-002/lectures/InfixToPostfixExamples.pdf
		# http://www.programmersheaven.com/2/Art_Expressions_p1
		#
		# Operator priorities are taken from:
		# Principles of Model Checking by Baier, pg.232
		# http://www.voronkov.com/lics_doc.cgi?what=chapter&n=14
		# Logic in Computer Science by Huth and Ryan, pg.177

		# Operator priorities (higher number means higher priority)
		operators = { "I": 0, "|" : 1, "&": 1, "U": 2, "G": 3, "F": 3, "X": 3, "!": 3};
		output = []
		stack = []

		# Remove leading, trailing, multiple white-space, and
		# split string at whitespaces
		formula = re.sub(r'\s+',' ',formula).strip().split()

		# Reverse the input
		formula.reverse()

		# Invert the parantheses
		for i in range(0,len(formula)):
			if formula[i] == '(':
				formula[i] = ')'
			elif formula[i] == ')':
				formula[i] = '('

		# Infix to postfix conversion
		for entry in formula:

			if entry == ')':
				# Closing paranthesis: Pop from stack until matching '('
				popped = stack.pop()
				while stack and popped != '(':
					output.append(popped)
					popped = stack.pop()

			elif entry == '(':
				# Opening paranthesis: Push to stack
				# '(' has the highest precedence when in the input
				stack.append(entry)

			elif entry not in operators:
				# Entry is an operand: append to output
				output.append(entry)

			else:
				# Operator: Push to stack appropriately
				while True:
					if not stack or stack[-1] == '(':
						# Push to stack if empty or top is '('
						# '(' has the lowest precedence when in the stack
						stack.append(entry)
						break
					elif operators[stack[-1]] < operators[entry]:
						# Push to stack if prio of top of the stack
						# is lower than the current entry
						stack.append(entry)
						break
					else:
						# Pop from stack and try again
						popped = stack.pop()
						output.append(popped)

		# Pop remaining entries from the stack
		while stack:
			popped = stack.pop()
			output.append(popped)

		# Reverse the order and join entries w/ space
		output.reverse()
		formula = ' '.join(output)

		return formula

	def fsa_from_cosafe_formula(self, formula):

		# scheck expects a prefix co-safe ltl formula w/ props: p0, p1, ...

		# Get the set of propositions
		props = re.sub('[IGFX!\(\)&|U]', ' ', formula)
		# TODO: implement true/false support
		props = set(re.sub('\s+', ' ', props).strip().split())

		# Form the bitmap dictionary of each proposition
		# Note: range goes upto rhs-1
		self.props = dict(zip(props, map(lambda x: 2 ** x, range(0, len(props)))))
		self.name = 'FSA corresponding to formula: %s' % (formula)
		self.final = set()
		self.init = {}

		# Alphabet is the power set of propositions, where each element
		# is a symbol that corresponds to a tuple of propositions
		# Note: range goes upto rhs-1
		self.alphabet = set(range(0, 2 ** len(self.props)))

		# Prepare from/to scheck conversion dictionaries
		i = 0
		to_scheck = dict()
		from_scheck = dict()
		for p in props:
			scheck_p = 'p%d'%i
			from_scheck[scheck_p] = p
			to_scheck[p] = scheck_p
			i += 1

		# Convert infix to prefix
		scheck_formula = Fsa.infix_formula_to_prefix(formula)
		# Scheck expect implies operator (I) to be lower-case
		scheck_formula = ''.join([i if i != 'I' else 'i' for i in scheck_formula])

		# Convert formula props to scheck props
		for k,v in to_scheck.items():
			scheck_formula = scheck_formula.replace(k, v)

		# Write formula to temporary file to be read by scheck
		import tempfile
		tf = tempfile.NamedTemporaryFile()
		tf.write(scheck_formula)
		tf.flush()

		# Execute scheck and get output
		try:
			lines = sp.check_output([scheck_binary, '-s', '-d', tf.name]).splitlines()
		except Exception as ex:
			raise Exception(__name__, "Problem running %s: '%s'" % (scheck_binary, ex))

		# Close temp file (automatically deleted)
		tf.close()

		# Convert lines to list after leading/trailing spaces
		lines = map(lambda x: x.strip(), lines)
		#for l in lines: print l
		#print '###############'

		# 1st line: "NUM_OF_STATES NUM_OF_ACCEPTING_STATES"
		# if NUM_OF_ACCEPTING_STATES is 0, all states are accepting
		l = lines.pop(0)
		state_cnt, final_cnt = map(int, l.split())
		if final_cnt == 0:
			final_cnt = state_cnt
			all_accepting = True
		else:
			all_accepting = False

		# Set of remaining states
		rem_states = set(['%s'%i for i in range(0,state_cnt)])

		# Parse state defs
		while True:
			# 1st part: "STATE_NAME IS_INITIAL -1" for regular states
			# "STATE_NAME IS_INITIAL ACCEPTANCE_SET -1" for final states
			l = lines.pop(0).strip().split()
			src = l[0]
			is_initial = True if l[1] != '0' else False
			is_final = True if len(l) > 3 else False

			# Mark as done
			rem_states.remove(src)

			# Mark as initial/final if required
			if is_initial:
				self.init[src] = 1
			if is_final:
				self.final.add(src)

			while True:
				# 2nd part: "DEST PREFIX_GUARD_FORMULA" 
				l = lines.pop(0).strip().split()
				if l == ['-1']:
					# Done w/ this state
					break
				dest = l[0]
				l.pop(0)
				guard = ''
				# Now l holds the guard in prefix form
				if l == ['t']:
					guard = '(1)'
				else:
					l.reverse()
					stack = []
					for e in l:
						if e in ['&', '|']:
							op1 = stack.pop()
							op2 = stack.pop()
							stack.append('(%s %s %s)' % (op1, e, op2))
						elif e == '!':
							op = stack.pop()
							stack.append('!%s' % (op))
						else:
							stack.append(e)
					guard = stack.pop()

				# Convert to regular props
				for k,v in from_scheck.items():
					guard = guard.replace(k,v)
				bitmaps = self.get_guard_bitmap(guard)
				#print '%s -[ %s (%s) ]-> %s (init: %s, final: %s)' % (src, guard, bitmaps, dest, is_initial, is_final)
				self.g.add_edge(src, dest, None, {'weight': 0, 'input': bitmaps, 'guard' : guard, 'label': guard})

			if not rem_states:
				break

		# We expect a deterministic FSA
		assert(len(self.init)==1)

		return

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

	def add_trap_state(self):

		trap_added = False
		for s in self.g.nodes():
			rem_alphabet = set([i for i in self.alphabet])
			for u,v,d in self.g.out_edges_iter(s,data=True):
				rem_alphabet -= d['input']
			if rem_alphabet:
				if 'trap' not in self.g:
					self.g.add_node('trap')
					self.g.add_edge('trap','trap', None, {'weight': 0, 'input': self.alphabet, 'guard': '(1)', 'label': '(1)'})
					trap_added = True
				self.g.add_edge(s,'trap', None, {'weight': 0, 'input': rem_alphabet, 'guard': 'trap_guard', 'label': 'trap_guard'})

		if not trap_added:
			logger.info('No trap states were added.')
		else:
			logger.info('Trap states were added.')

	def symbols_w_prop(self, prop):
		return set(filter(lambda symbol: True if self.props[prop] & symbol else False, self.alphabet))

	def symbols_wo_prop(self, prop):
		return self.alphabet.difference(self.symbols_w_prop(prop))

	def bitmap_of_props(self, props):
		prop_bitmap = reduce(lambda x, y: x | y, map(lambda p: self.props.get(p, 0), props), 0)
		return prop_bitmap

	def next_states_of_fsa(self, q, props):
		# Get the bitmap representation of props
		prop_bitmap = self.bitmap_of_props(props)

		# Return an array of next states
		return filter(lambda x: True if x is not None else False,
							# next state if bitmap is in inputs else None
							map(lambda e: e[1] if prop_bitmap in e[2]['input'] else None,
							# Get all edges from q
							self.g.out_edges_iter(q,True)))
