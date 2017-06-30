import pdb
class Finite_Automata(object):
    
    def __init__(self):
        self.name = ""
        self.initials = ""
        self.finals = []
        self.transitions = {}
        self.alphabet = set() 
        self.states = []
        #	[transitions, final, initial]
        #	Example state: 
        #	q0 = [[a : q2, b : q3], false, true]
   
    def set_name(self, name):
        self.name = name

    def calculate_alphabet(self):
        new_alphabet = set()
        for q in self.transitions.keys():
            for k in self.transitions[q].keys():
                if k not in new_alphabet:
                    new_alphabet.add(k)
        self.alphabet = {x for x in new_alphabet}

    def add_final(self, name_state):
        if self.verify_name(name_state):
            name = self.equi_name(name_state)
            if name not in self.finals:
                self.finals.append(name)

    def add_initial(self, name_state):
        self.initials = name_state

    def equi_name(self, name):
        resultado = False
        avaliar = set(name.split(', '))
        for estado in self.states:
            estado_split = set(estado.split(', '))
            if avaliar ^ estado_split == set():
                resultado = True
            if resultado:
                break
        return estado

    def verify_name(self, name):
        resultado = False
        avaliar = set(name.split(', '))
        for estado in self.states:
            estado_split = set(estado.split(', '))
            if avaliar ^ estado_split == set():
                resultado = True
            if resultado:
                break
        return resultado
    
    def create_state(self, name, initial, final):
        if not self.verify_name(name):
            if initial:
                self.initials = name
            if final:
                self.finals.append(name)
            self.states.append(name)

    def delete_state(self, name):
        if name not in self.states:
            print("state not found")
            return
        self.states.remove(name)
        if name in self.transitions.keys():
            del self.transitions[name]
        states = list(self.transitions.keys())
        for q in states:
            keys = list(self.transitions[q].keys())
            for key in keys:
                #trans_split = self.transitions[q][key].split(", ")
                #if name in trans_split:
                #    trans_split.remove(name)
                #    self.transitions[q][key] = ""
                #    for st in trans_split:
                #        self.transitions[q][key] += ", "+st
                if self.transitions[q][key] is name:
                    del self.transitions[q][key]
        self.calculate_alphabet()
        if name == self.initials:
            self.initials = ""
        if name in self.finals:
            self.finals.remove(name)

    def create_transition_aux(self, name):
        if name not in self.transitions.keys():
            self.transitions[name] = {}

    def create_transition(self, name_state1, name_state2, key):
        name1 = name_state1
        name2 = name_state2
        if name1 not in self.states:
            if not self.verify_name(name_state1):
                self.create_state(name_state1, False, False)
            else:
                name1 = self.equi_name(name_state1)
        if name2 not in self.states:
            if not self.verify_name(name_state2):
                self.create_state(name_state2, False, False)
            else:
                name2 = self.equi_name(name_state2)
        self.create_transition_aux(name1)
        if key in self.transitions[name1].keys():
            split = set(self.transitions[name1][key].split(', '))
            name_state2_split = set(name2.split(', '))
            simmetric_diff = name_state2_split ^ split
            if simmetric_diff == set():
                self.transitions[name1][key] += ', '+name2
            else:
                diff = name_state2_split - split
                for d in diff:
                    self.transitions[name1][key] += ', '+d
        else:
            self.transitions[name1][key] = name2
        if key not in self.alphabet:
            self.alphabet.add(key)
       
    def delete_transition(self, name_state1, name_state2, key):
        if name_state1 not in self.transitions.keys():
            print("state not found")
            return
        state1_keys = list(self.transitions[name_state1])
        if key not in state1_keys:
            print("key not found")
            return
        if name_state2 not in self.transitions[name_state1][key]:
            print("transition not found")
            return
        trans_split = self.transitions[name_state1][key].split(", ")
        trans_split.remove(name_state2)
        if trans_split != []:
            self.transitions[name_state1][key] = ""
            for t in trans_split:
                self.transitions[name_state1][key] += t
        self.calculate_alphabet()

    def delete_all_transitions(self, name_state, key):
        if name_state not in self.transitions.keys():
            print("state not found")
            return
        state_keys = list(self.transitions[name_state])
        if key not in state_keys:
            print("key not found")
            return
        del self.transitions[name_state][key]
        self.calculate_alphabet()
