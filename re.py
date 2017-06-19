from Finite_Automata import Finite_Automata
import copy

alphabet = set()
non_alphabet = set(['*', '.', '|', '?'])

class Node:
    def __init__(self, expression, root):
        re = self.remove_edge_parenthesis(expression)
        self.left = None
        self.right = None
        self.father = root
        self.next = None
        self.count = 0

        # if is the last character to be computed
        #print('')
        #print('Creating node, my expression: ' + re)
        if len(expression) == 1:
            self.operator = re[0]
            #print('Creating node, operator: ' + self.operator)
            #print('I am a leaf')

        else:
            # find the next operator to compute, and find its index
            # print(re)
            index = self.index_symbol(re)
            if type(index) is int:
                self.operator = re[index]
            else:
                self.operator = re[0]
            #print('Creating node, operator: ' + self.operator)
            # section the entry expression into right or left
            l_string = re[0:index]
            #print('My left string will have: ' + str(l_string))
            # if it isn't the last character on the right
            if (index + 1) != len(re):
                r_string = re[index+1:]
            else:
                r_string = None
            #print('My right string will have: ' + str(r_string))
            # if there is something on the right or left, make a node out of it
            if l_string:
                self.left = Node(l_string, self)
            if r_string:
                self.right = Node(r_string, self)

    # going up
    def up(self, composition, up):
        #print("Up - node : " + str(self.count)+ ' - ' + self.operator)
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
        elif self.operator == '|':
            if self.father is None:
                composition.append(None)
            else:
                self.father.up(composition, up)
        # else, it's a symbol from the alphabet, add it to the list
        else:
            composition.append(self)

    def up_start(self):
        #print("Starting down operation from: " + str(self.count)+ ' - ' + self.operator)
        composition = list()
        up = set()
        self.up(composition, up)
        return composition

    # going down
    def down(self, composition, up):
        #print("Down - node : " + str(self.count)+ ' - ' + self.operator)
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
        elif self.operator == '|':
            self.left.down(composition, up)
            self.right.down(composition, up)
        # else, it's a symbol from the alphabet, add it to the list
        else:
            composition.append(self)

    def down_start(self):
        #print("Starting down operation: " + str(self.count)+ ' - ' + self.operator)
        composition = list()
        up = set()
        self.down(composition, up)
        return composition

    # links the list and numbers each position
    def link_start(self):
        #print("Starting link operation: " + str(self.count)+ ' - ' + self.operator)
        self.count = 0
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
        #print("Link operation, I am: " + str(self.count)+ ' - ' + self.operator)
        #print('')
        if self.right is not None:
            number = self.right.link_count(self.count, composition)

        return number

    def link(self, composition):
        if self.left is not None:
            self.left.link(composition)
        if len(composition) == self.count:
            self.next = None
            #print('Node: ' + str(self.count) + ' - ' + self.operator + '. My next is: None')
        elif len(composition) != self.count:
            self.next = composition[self.count]
            #print('Node: ' + str(self.count) + ' - ' + self.operator + '. My next is: ' + str(self.next.count) + ' - ' + self.next.operator)
        if self.right is not None:
            self.right.link(composition)

    def remove_edge_parenthesis(self, expression):
        parenthesis = 0
        end = False
        if len(expression) > 0:
            if expression[0] == '(' and expression[-1] == ')':
                # checks if it's the same parenthesis opening
                for char in expression:
                    # ends and doesnt return expression if it was suposed to be the last character
                    # but wasn't
                    if end:
                        return expression
                    if char == '(':
                        parenthesis += 1
                    elif char == ')':
                        parenthesis -= 1
                        if parenthesis == 0:
                            end = True

        if parenthesis == 0 and end:
            return expression[1:-1]
        else:
            return expression

    # Returns the index of the symbol of least priority on the string received
    def index_symbol(self, re):
        parenthesis = 0
        for symbol in '|.*?':
            for index, char in enumerate(re):
                if char == '(':
                    parenthesis += 1
                elif char == ')':
                    parenthesis -= 1
                elif parenthesis == 0 and char == symbol:
                    #print('index returned: ' + str(index))
                    return index
        return re


# adds '.' to separate alphabet characters, adds characters to alphabet
def dot_placer(re, alphabet):
    first = True
    new_re = ''
    alphabet.clear()

    for char in re:
        if char not in non_alphabet:
            alphabet.add(char)
            if first:
                if char == '(':
                    pass
                else:
                    first = False
            else:
                # if char is ')', the dot isnt needed
                if char != ')':
                    # if char is '(', there wont be a dot afterwards
                    if char == '(':
                        first = True   
                    new_re += '.'
        else:
            if char == '*':
                pass
            else:
                first = True
        new_re += char
    if '(' in alphabet:
        alphabet.remove('(')
    if ')' in alphabet:
        alphabet.remove(')')
    return new_re

def de_simone(re):
    alphabet = set()
    non_alphabet = set(['*', '.', '|', '?'])
    # adding . to separate letters
    tree = dot_placer(re, alphabet)
    # starts recursive tree creation
    root = Node(tree, None)

    # links the whole tree
    root.link_start()
    
    # first list of nodes to be computed
    nodes = root.down_start()
    print('nodes length: ' + str(len(nodes)))

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

    print("my alphabet: " +str(alphabet))

    # for each node in the tree, check if it's  operator or None and add it to composition
    for node in nodes:
        if node is None:
            final = True
            composition.add(None)
        else:
            if node.operator in alphabet:
                composition.add(node)
                transitions.add(str(node.operator))

    composure = list()
    for component in composition:
        if component is not None:
            composure.append(str(component.count) + '-' + component.operator)
        else:
            composure.append(None)
    print('Compositions: ' + str(composure))
    new_states = list()
    new_states.append([copy.copy(transitions), copy.copy(composition), final, 0])


    final = False

    # set to hold the next transitions of the state 
    temp_transitions = set()

    composition.clear()
    transitions.clear()
    # while new states are found
    while new_states:
        # for each state found
        #for new_state in new_states:
        print('Computing state ' + str(new_states[0][3]) + ': ' + str(new_states[0][0]))
        # for each transition in the previous state, check all elements and see where they can reach
        for no, transition in enumerate(new_states[0][0]):
            if ':' not in transition:   
                temp_transitions.add(transition)
                final = False
                print()
                print('Examining transition: ' + transition)
                for element in new_states[0][1]:
                    # if the right operator
                    if element is not None and element.operator == transition:
                        # for each element, create what it can access
                        print('Element is equal to transition, element is: ' + str(element.count) + '-' + element.operator)
                        if element.next is None:
                            final = True
                            composition.add(None)
                            nodes = list()
                        else:
                            nodes = element.next.up_start()
                        print('Number of nodes found: ' + str(len(nodes)))
                        for index, node in enumerate(nodes):
                            if node is None:
                                final = True
                                composition.add(None)
                            else:
                                print('Node: ' + str(node.count) + '-' + node.operator)
                                if node.operator in alphabet:
                                    composition.add(node)
                                    transitions.add(str(node.operator))
                print()
                print('Transition checked, verifying if composition already exists')
                # checks if the state already exists, by checking its composition
                exists = False

                for index, state in enumerate(states):
                    print('Checking state ' + str(index))
                    # composition needs to be the exact size
                    if len(state[1]) == len(composition):
                        exists = True
                        for node in state[1]:
                            if node not in composition:
                                exists = False
                        # if it exists, set the transition to that state
                        if exists:
                            if transition in transitions:
                                transitions.remove(transition)
                            transitions.add(str(transition + ':q' + str(index)))
                            if transition in temp_transitions:
                                temp_transitions.remove(transition) 
                            temp_transitions.add(str(transition + ':q'+ str(index)))
                            break
                if not exists:
                    for index, state in enumerate(new_states):
                        print('Checking new state ' + str(index))
                        # composition needs to be the exact size
                        if len(state[1]) == len(composition):
                            exists = True
                            for node in state[1]:
                                if node not in composition:
                                    exists = False
                            # if it exists, set the transition to that state
                            if exists:
                                if transition in transitions:
                                    transitions.remove(transition)
                                transitions.add(str(transition + ':q' + str(index + len(states))))
                                if transition in temp_transitions:
                                    temp_transitions.remove(transition) 
                                temp_transitions.add(str(transition + ':q'+ str(index + len(states))))
                                break
                print('State exists: ' + str(exists))
                # if the state did exist, change transition to it. Else create the state
                if not exists:
                    if transition in temp_transitions:
                                temp_transitions.remove(transition)
                    temp_transitions.add(transition + ':q'+ str(len(states) + len(new_states)))
                    print('Transition was: ' + transition)
                    print('Transition changed to: ' + transition + ':q'+ str(len(states) + len(new_states)))
                    print('')
                    print('Created new State:')
                    print('Transitions: ' + str(transitions))
                    composure = list()
                    for component in composition:
                        if component is not None:
                            composure.append(str(component.count) + '-' + component.operator)
                        else:
                            composure.append(None)
                    print('Compositions: ' + str(composure))
                    new_states.append([copy.copy(transitions), copy.copy(composition), final, len(states) + len(new_states)])
                print('Final transitions: ' + str(transitions))
                composition.clear()
                transitions.clear()
        new_states[0][0] = copy.copy(temp_transitions)
        temp_transitions.clear()

        # adds all new states to checked states
        print()
        print('------ Finished Transitions ------')
        states.append(new_states.pop(0))

        # set new states as all those found out
        print(' States remaining: ' + str(len(new_states)))

    # now all is left is to create the state machine
    fa = Finite_Automata()

    print()
    print('------ Finished State Creations -------')
    print('Expression: ' + re)
    print('States: ')
    for index, state in enumerate(states):
        # name, initial, final
        name = 'q' + str(index)
        print()
        print('State: ' + name)
        print('Transitions: ' + str(state[0]))
        composure = list()
        for component in state[1]:
            if component is not None:
                composure.append(str(component.count) + '-' + component.operator)
            else:
                composure.append(None)
        print('Compositions: ' + str(composure))
        fa.create_state(name, 0, state[2])
        for transition in state[0]:
            splitted = transition.split(':')
            print('splitted transition: ' + str(splitted))
            if len(splitted) == 2:
                fa.create_transition(name, 'q' + str(splitted[1]), splitted[0])
            else:
                print('something is wrong')

    fa.add_initial('q0')

    print('---------------------------------------')
    print('----------------Ended------------------')
    print('---------------------------------------')

    return fa

if __name__ == '__main__':
    strings = ['a|a*c', '(a|b)', '((a|b)*ab)', 'a?((b|a(ba*))*)']
    finite_automatas = list()

    for element in strings:
        print(dot_placer(element, set()))
        finite_automatas.append(de_simone(element))
