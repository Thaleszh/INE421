import Finite_Automata

def minimize(fa):
    #verificar estados acessiveis
    acessiveis = set(x for x in fa.initials)
    new_acessiveis = set()
    while acessiveis != new_acessiveis:
        new_acessiveis = acessiveis
        for s in acessiveis:
            for a in fa.transitions[s].keys():
                new_acessiveis.add(fa.transitions[s][a])

    for st in fa.states not in acessiveis:
        fa.delete_state(st)

    #verificar estados mortos
    vivos = set(x for x in fa.finals)
    new_vivos = set()
    while vivos != new_vivos:
        new_vivos = vivos
        for state in vivos
            for s in fa.states 
                for a in fa.transitions[s].keys():
                    if fa.transitions[s][a] is state
                        new_vivos.add(s)

    for st in fa.states not in vivos:
        fa.delete_state(st)

    #achar estados equivalentes
    for a in self.alphabet:
        fa.create_transition2("Fi", "Fi", a)
    
    for s in self.states:
        for k in self.alphabet not in self.transitions[s].keys():
            fa.create_transition2(s, "Fi", k)

    set_F = {x for x in fa.finals}
    set_KF = {x for x in fa.states not in finals}

    algorithm_sets = [set_F, set_KF]

    change = True
    while change:
        aux_algorithm_sets = []
        change = False
        for analysis_set in algorithm_sets:
            equivalence = {}
            for s in analysis_set:
                equivalence[s] = {}
                for a in fa.alphabet:
                    for x in range(0, len(algorithm_sets-1))
                        if fa.transitions[s][a] in algorithm_sets[x]
                            equivalence[s][a] = x
            keys = [x for x in analysis_set]
            equivalent = False
            while keys != []:
                analysing = keys.pop()
                aux_algorithm_sets.append(set(analysing))
                for k in keys:
                    for a in fa.alphabet:
                        if equivalence[analysing][a] == equivalence[k][a]:
                            equivalent = True
                        else:
                            equivalent = False
                            break
                    if equivalent:
                        aux_algortihm_sets[-1].add(k)
                        keys.remove(k)
        if aux_algorithm_sets != algorithm_sets:
            change = True
            algorithm_sets = aux_algorithm_sets

    new_initial = ""
    new_finals = []
    new_transitions = {}

    FA_Min = Finite_Automata()

    for x in range(0, len(algorithm_sets)-1):
        FA_Min.create_state2(x, False, False)
        new_transitions[x] = {}
        for e in algorithm_sets[x]:
            if e == fa.initials:
                new_initial = x
            if e in fa.finals:
                new_finals += x
        for a in fa.alphabet:
            new_transitions[x][a] = equivalence[e][a]

    FA_Min.initials = new_initial
    FA_Min.finals = list(set(new_finals))
    FA_Min.transitions = new_transitions

    return FA_Min

def determinize(fa):
    for s in fa.transitions.keys():
        for k in fa.transitions.[s].keys():
            state = fa.transitions.[s][k]
            if state not in fa.states:
                each_state = state.split(", ")
                state_final = False
                for t in each_state:
                    if t in fa.finals:
                        state_final = True
                fa.create_state2(state, False, state_final)
                for t in each_state:
                    for a in fa.alphabet:
                        fa.create_transition2(state, fa.transition[t][a], a)


def union(fa1, fa2):
    fa3 = Finite_Automata()

    fa3.alphabet = fa1.alphabet + fa2.alphabet
    fa3.states = fa1.states + fa2.states
    fa3.finals = fa1.finals + fa2.finals

    new_initial_final = False

    if fa1.initials[0] in fa1.finals:
        new_initial_final = True
    if fa2.initials[0] in fa2.finals:
        new_initial_final = True

    fa3.create_state2(fa1.initials[0]+", "+fa2.initials[0],
                      True, new_initial_final)
    
    for k in fa1.transitions[fa1.initials[0]].keys():
        fa3.create_transition(fa3.initials[0], 
                              fa1.transitions[fa1.initials[0]][k],
                              [k])
    for k in fa2.transitions[fa2.initials[0]].keys():
        fa3.create_transition(fa3.initials[0], 
                              fa2.transitions[fa2.initials[0]][k],
                              [k])

    for s in fa1.states:
        for k in fa1.transitions[s].keys():
            fa3.create_transition2(s,fa1.transitions[s][k], k)

    for s in fa2.states:
        for k in fa2.transitions[s].keys():
            fa3.create_transition2(s,fa2.transitions[s][k], k)

    determinize(fa3)
    return(fa3)

def complement(fa1):
    fa2 = Finite_Automata([])
    fa2.initials = fa1.finals
    fa2.finals = fa1.initials
    fa2.transitions = fa1.transitions
    return fa2

def intersection(fa1, fa2):
    return complement(union(complement(fa1), complement(fa2)))

def dif(fa1, fa2):
    return intersection(fa1, complement(fa2))
