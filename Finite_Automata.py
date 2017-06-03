

class Finite_Automata(object):
    initials = []
    finals = []
    transitions = {}
    
    def __init__(self):
        pass

    def __init__(self, states):
        #	[transitions, final, initial]
        #	Example state: 
        #	q0 = [[a : q2, b : q3], false, true]
    
        for state in states:
            if state[2] is True:
                self.initials.append(state[0])
            if state[3] is True:
                self.finals.append(state[0])
            self.transitions[state[0]] = state[1]
        
    def create_state(state):
        if state[2] is True:
            self.initials.append(state[0])
        if state[3] is True:
            self.finals.append(state[0])
        self.transitions[state[0]] = state[1]

    def create_state(name, transitions, initial, final):
        if initial is True:
            self.initials.append(name)
        if final is True:
            self.finals.append(name)
        self.transitions[name] = [transitions]

    def create_transition(state1, state2, key):
        states = list(transitions.keys())
        if state1 not in states:
            create_state(state1[0], state1[1], state1[2], state1[3])
        if state2 not in states:
            create_state(state2[0], state2[1], state2[2], state2[3])
        self.transitions[state1[0]][key] = state2[0]



class State:
    info = []

    def __init__(self, name, transitions, initial, final):
        self.info = [name, transitions, initial, final]
