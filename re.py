from Finite_Automata import Finite_Automata

alphabet = set()
non_alphabet = set(['*', '.', '|', '?'])

class node:
    def __init__(self, expression, root):
        re = remove_edge_parenthesis(expression)
        self.left = None
        self.right = None
        self.father = root
        self.next = None
        self.count = 0

        # if is the last character to be computed
        if len(expression) == 1:
            self.operator = re[0]
        else:
            # find the next operator to compute, and find its index
            index = index_symbol(re)
            self.operator = re[index]
            # section the entry expression into right or left
            l_string = re[0:index]
            # if it isn't the last character on the right
            if (index + 1) != len(re):
                r_string = re[index+1:]
            # if there is something on the right or left, make a node out of it
            if l_string:
                self.left = Node(l_string, self)
            if r_string:
                self.right = Node(r_string, self)

    # going up
    def up(self, composition, up):
        # if its a * go down and up from the next
        if self.operator == '*':
            # if it's the first time passing
            if self not in up:
                up.add(self)
                self.left.down(composition, up)
                if self.next is None:
                    composition.append(None)
                else:
                    self.next.up(composition, up)
        # if it's ? go up from the next
        elif self.operator == '?':
            if self.next is None:
                composition.append(None)
            else:
                self.next.up(composition, up)
        # if it's . go down the right
        elif self.operator == '.':
            self.right.down(composition, up)
        # if it's | go to father
        elif self.operator == '|'
            if self.father is None:
                composition.append(None)
            else:
                self.father.up(composition, up)
        # else, it's a symbol from the alphabet, add it to the list
        else:
            composition.append(self)

    def up(self):
        composition = list()
        up = set()
        up.add(self)
        self.up(composition, up)
        return composition

    # going down
    def down(self, composition, up):
        # if it's * or ? go down left and up to the next
        if self.operator in {'*', '?'}:
            self.left.down(composition, up)
            if self.next is None:
                composition.append(None)
            else:
                self.next.up(composition, up)
        # if . go down left
        elif self.operator == '.':
            self.left.down(composition, up)
        # if it's | go to both options
        elif self.operator == '|'
            self.left.down(composition, up)
            self.right.down(composition, up)
        # else, it's a symbol from the alphabet, add it to the list
        else:
            composition.append(self)

    def down(self):
        composition = list()
        up = set()
        self.down(composition, up)
        return composition

    # links the list and numbers each position
    def link(self):
        self.count = 1
        composition = list()
        self.link_count(self.count, composition)
        self.link(composition)

    # linking number of each node by order: left, self, right
    def link_count(self, number, composition):
        if self.left is None:
            self.count = 1 + number
        else:
            self.count = 1 + self.left.link_count(number, composition)        
        number = self.count
        composition.append(self)
        if self.right is not None:
            number = self.right.link_count(self.count, composition)

        return number

    def link(self, composition):
        if self.left is not None:
            self.left.link(composition)
        if len(composition) != self.count:
            self.next = composition[self.count]
        if self.right is not None:
            self.right.link(composition)


def de_simone(re):
    alphabet = set()
    non_alphabet = set(['*', '.', '|', '?'])
    # adding . to separate letters
    tree = dot_placer(re)
    # starts recursive tree creation
    root = node(tree, None)
    # links the whole tree
    root.link()
    
    fa = Finite_Automata()
    # first list of nodes to be computed
    nodes = root.down()

    # set of leaf-nodes that compose the determined state
    composition = set()
    # if determined state would reach the final
    final = False
    # set of transitions
    # transition = symbol:state
    # or
    # transition = symbol
    transitions = set()

    # list of states
    # state = [set of strings, set of nodes, boolean]
    # state = [transitions, composition, final]
    states = list()

    # for each node in the tree, check if it's  operator or None and add it to composition
    for node in nodes:
        if node is None:
            final = True
            composition.add(None)
        else:
            if node.operator in alphabet:
                composition.add(node)
                transitions.add(node.operator)

    states.append([transitions, composition, final])
    composition.clear()
    transitions.clear()
    final = False
    i = 1

    # set to hold the next transitions of the state 
    temp_transitions = set()
    new_states = list()

    # for each transition in the previous state, check all elements and see where they can reach
    for transition in states[i-1][0]:
        for element in states[i-1][1]:
            # if the right operator
            if element.operator == transition:
                # for each element, create what it can access
                nodes = element.next.up()
                for node in nodes:
                    if node is None:
                        final = True
                        composition.add(None)
                    else:
                        if node.operator in alphabet:
                            composition.add(node)
                            transitions.add(node.operator)

        # checks if the state already exists, by checking its composition
        exists = False
        for index, state in enumerate(states):
            # composition needs to be the exact size
            if len(state[1]) == len(composition):
                exists = True
                for node in state[1]:
                    if node not in composition:
                        exists = False
                # if it exists, set the transition to that state
                if exists:
                    temp_transitions.remove(transition)
                    temp_transitions.add(transition + ':'+ str(index))
                    break
        # if the state did not exist
        if not exists:
            new_states.append([transitions, composition, final])












# Returns the index of the symbol of least priority on the string received
def index_symbol(re):
    parenthesis = 0
    for symbol in '|.*?'
        for index, char in enumerate(re):
            if char == '(':
                parenthesis += 1
            elif char == ')':
                parenthesis -= 1
            elif parenthesis == 0 and char == symbol:
                return index
    return re


# adds '.' to separate alphabet characters, adds characters to alphabet
def dot_placer(re):
    first = True
    new_re = ''
    alphabet.clear()

    for index, char in enumerate(re):
        if char not in non_alphabet:
            alphabet.add(char)
            if first:
                first = False
            else:
                # if char is ')', the dot isnt needed
                if char != ')':
                    new_re += '.'
                    # if char is '(', there wont be a dot afterwards
                    if char == '(':
                        first = True
        else:
            first = True
        new_re += char
    alphabet.remove('(')
    alphabet.remove(')')
    return new_re

def remove_edge_paranthesis(expression):
    edge = expression
    if len(edge) > 0:
        if edge[0] == '(' and edge[-1] == ')':
            return edge[1:-1]
    return edge
