

class Finite_Automata(object):
    
    def __init__(self):
        self.initials = []
        self.finals = []
        self.transitions = {}
        self.alphabet = [] 
        self.states = []
        #	[transitions, final, initial]
        #	Example state: 
        #	q0 = [[a : q2, b : q3], false, true]
   
    def calculate_alphabet(self):
        new_alphabet = []
        for q in self.transitions.keys():
            for k in self.transitions[q].keys():
                if k not in new_alphabet:
                    new_alphabet.append(k)
        self.alphabet = new_alphabet

    def add_final1(state):
        if state.final:
            self.finals.append(state.name)

    def add_initial1(state):
        if state.initial:
            self.initials.append(state.name)

    def add_final2(name_state):
        self.finals.append(name_state)

    def add_initial2(name_state):
        self.initials.append(name_state)

    def create_state1(self, state):
        if state.initial:
            self.initials.append(state.name)
        if state.final:
            self.finals.append(state.name)
        self.states.append(state.name)

    def create_state2(self, name, initial, final):
        if initial:
            self.initials.append(name)
        if final:
            self.finals.append(name)
        self.states.append(name)

    def delete_state1(self, state):
        if state.name not in self.states:
            print("state not found")
            return
        self.states.remove(state.name)
        del self.transitions[state.name]
        states = list(self.transitions.keys())
        for q in states:
            keys = list(self.transitions[q].keys())
            for key in keys:
                if state.name not in keys:
                    pass
                if self.transitions[q][key] is state.name:
                    del self.transitions[q][key]
        self.calculate_alphabet()
        if state.name in self.initials:
            self.initials.remove(state.name)
        if state.name in self.finals:
            self.finals.remove(state.name)

    def delete_state2(self, name):
        if name not in self.states:
            print("state not found")
            return
        self.states.remove(name)
        del self.transitions[name]
        states = list(self.transitions.keys())
        for q in states:
            keys = list(self.transitions[q].keys())
            for key in keys:
                if name not in keys:
                    pass
                if self.transitions[q][key] is name:
                    del self.transitions[q][key]
        self.calculate_alphabet()
        if name in self.initials:
            self.initials.remove(name)
        if name in self.finals:
            self.finals.remove(name)

    def create_transition_aux(self, name):
        if name not in self.transitions.keys():
            self.transitions[name] = {}

    def create_transition1(self, state1, state2, key):
        if state1.name not in self.states:
            self.create_state1(state1)
        if state2.name not in self.states:
            self.create_state1(state2)
        self.create_transition_aux(state1.name)
        if key in self.transitions[state1.name].keys():
            self.transitions[state1.name][key] += ", "+state2.name
        else:
            self.transitions[state1.name][key] = state2.name
        self.calculate_alphabet()

    def create_transition2(self, name_state1, name_state2, key):
        if name_state1 not in self.states:
            self.create_state2(name_state1, False, False)
        if name_state2 not in self.states:
            self.create_state2(name_state2, False, False)
        self.create_transition_aux(name_state1)
        if key in self.transitions[name_state1].keys():
            self.transitions[name_state1][key] += ", "+name_state2
        else:
            self.transitions[name_state1][key] = name_state2
        self.calculate_alphabet()

    def delete_transition1(self, state1, state2, key):
        if state1.name not in self.states:
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
        self.calculate_alphabet()
        
    def delete_transition2(self, name_state1, name_state2, key):
        if name_state1 not in self.states:
            print("state not found")
            return
        state1_keys = list(self.transitions[name_state1])
        if key not in state1_keys:
            print("key not found")
            return
        if name_state2 is not self.transitions[name_state1][key]:
            print("transition not found")
            return
        del self.transitions[name_state1][key]
        self.calculate_alphabet()
        

class State:

    def __init__(self, name, initial, final):
        self.name = name
        self.initial = initial
        self.final = final
