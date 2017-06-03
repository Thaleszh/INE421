

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
            if state.initial is True:
                self.initials.append(state.name)
            if state.final is True:
                self.finals.append(state.name)
            self.transitions[state.name] = state.transitions
        
    def create_state(self, state):
        if state[2] is True:
            self.initials.append(state.name)
        if state[3] is True:
            self.finals.append(state.name)
        self.transitions[state.name] = state.transitions

    def create_state(self, name, transitions, initial, final):
        if initial is True:
            self.initials.append(name)
        if final is True:
            self.finals.append(name)
        self.transitions[name] = transitions

    def create_transition(self, state1, state2, key):
        states = list(self.transitions.keys())
        if state1.name not in states:
            self.create_state(state1.name, state1.transitions, state1.initial,
                    state1.final)
        if state2.name not in states:
            self.create_state(state2.name, state2.transitions, state2.initial,
                    state2.final)
        self.transitions[state1.name][key] = state2.name

    def delete_transition(self, state1, state2, key):
        states = list(self.transitions.keys())
        if state1.name not in states:
            print("state not found")
            return
        state1.keys = list(self.transitions[state1.name])
        if key not in state1.keys:
            print("key not found")
            return
        if state2.name is not self.transitions[state1.name][key]:
            print("transition not found")
            return
        del self.transitions[state1.name][key]
        

class State:
    name = ""
    transitions = {}
    initial = False
    final = False

    def __init__(self, name, transitions, initial, final):
        self.name = name
        self.transitions = transitions
        self.initial = initial
        self.final = final
