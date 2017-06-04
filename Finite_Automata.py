

class Finite_Automata(object):
    
    def __init__(self, states):
        self.initials = []
        self.finals = []
        self.transitions = {}
        self.alphabet = []
        #	[transitions, final, initial]
        #	Example state: 
        #	q0 = [[a : q2, b : q3], false, true]
    
        for state in states:
            if state.initial is True:
                self.initials.append(state.name)
            if state.final is True:
                self.finals.append(state.name)
            self.transitions[state.name] = state.transitions
            for k in state.transitions.keys():
                if k not in alphabet:
                    self.alphabet.append(k)
       
    def add_final(state):
        if state.final:
            self.finals.append(state.name)

    def add_initial(state):
        if state.initial:
            self.initials.append(state.name)

    def create_state1(self, state):
        if state.initial is True:
            self.initials.append(state.name)
        if state.final is True:
            self.finals.append(state.name)
        self.transitions[state.name] = state.transitions
        for k in state.transitions.keys():
            if k not in alphabet:
                self.alphabet.append(k)

    def create_state2(self, name, transitions, initial, final):
        if initial is True:
            self.initials.append(name)
        if final is True:
            self.finals.append(name)
        self.transitions[name] = transitions
        for k in state.transitions.keys():
            if k not in alphabet:
                self.alphabet.append(k)

    def delete_state(self, state):
        states = list(self.transitions.keys())
        if state.name not in states:
            print("state not found")
            return
        del self.transitions[state.name]
        states = list(self.transitions.keys())
        for q in states:
            keys = list(self.transitions[q].keys())
            for key in keys:
                if state.name not in keys:
                    pass
                if self.transitions[q][key] is state.name:
                    del self.transitions[q][key]
        if state.name in self.initials:
            self.initials.remove(state.name)
        if state.name in self.finals:
            self.finals.remove(state.name)

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
        state1_keys = list(self.transitions[state1.name])
        if key not in state1_keys:
            print("key not found")
            return
        if state2.name is not self.transitions[state1.name][key]:
            print("transition not found")
            return
        del self.transitions[state1.name][key]
        

class State:

    def __init__(self, name, transitions, initial, final):
        self.name = name
        self.transitions = transitions
        self.initial = initial
        self.final = final
