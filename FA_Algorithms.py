import Finite_Automata
import pdb

def minimize(fa):
    #verificar estados acessiveis
    acessiveis = set()
    acessiveis.add(fa.initials)
    aux_acessiveis = set()
    while acessiveis != aux_acessiveis:
        aux_acessiveis = {x for x in acessiveis} 
        for s in aux_acessiveis:
            for a in fa.transitions[s].keys():
                acessiveis.add(fa.transitions[s][a])

    states = [x for x in fa.states]
    for st in states:
        if st not in acessiveis:
            fa.delete_state2(st)

    #verificar estados mortos
    vivos = {x for x in fa.finals}
    aux_vivos = set()
    while vivos != aux_vivos:
        aux_vivos = {x for x in vivos}
        for s in fa.states:
            for a in fa.transitions[s].keys():
                if fa.transitions[s][a] in aux_vivos:
                    vivos.add(s)

    states = [x for x in fa.states]
    for st in states:
        if st not in vivos:
            fa.delete_state2(st)


    #achar estados equivalentes
    states = [x for x in fa.states]
    alphabet = [x for x in fa.alphabet]
    for s in states:
        for k in alphabet:
            if k not in fa.transitions[s].keys():
                fa.create_transition2(s, "Fi", k)

    if "Fi" in fa.states:
        for k in fa.alphabet:
            fa.create_transition2("Fi", "Fi", k)

    set_F = {x for x in fa.finals}
    set_KF = set()

    for s in fa.states:
        if s not in fa.finals:
            set_KF.add(s)

    algorithm_sets = [set_F, set_KF]
    if set_KF == set():
        algorithm_sets.remove(set_KF)
    aux_algorithm_sets = []
    equivalence = {}

    while algorithm_sets != aux_algorithm_sets:
        aux_algorithm_sets = [x for x in algorithm_sets]
        #print(aux_algorithm_sets)
        algorithm_sets = []
        for analysis_set in aux_algorithm_sets:
            #print(analysis_set)
            for s in analysis_set:
                #print(s)
                equivalence[s] = {}
                #print(equivalence)
                for a in fa.alphabet:
                    for x in range(0, len(aux_algorithm_sets)):
                        if s in fa.transitions.keys():
                            if fa.transitions[s][a] in aux_algorithm_sets[x]:
                                equivalence[s][a] = str(x)
            #print(equivalence)
            keys = [x for x in analysis_set]
            aux_keys = [x for x in analysis_set]
            #print(keys)
            equivalent = False
            while keys != []:
                analysing = keys.pop()
                #print(analysing)
                #print(keys)
                algorithm_sets.append(set())
                algorithm_sets[-1].add(analysing)
                #print(algorithm_sets)
                for k in aux_keys:
                    if k not in keys:
                        break
                    #print(k)
                    #print(aux_keys)
                    #print(keys)
                    for a in fa.alphabet:
                        if a in equivalence[analysing].keys():
                            if a in equivalence[k].keys():
                                if equivalence[analysing][a] == equivalence[k][a]:
                                    equivalent = True
                                else:
                                    equivalent = False
                                    break
                    if equivalent:
                        algorithm_sets[-1].add(k)
                        keys.remove(k)
                        #print(algorithm_sets)
        #print(algorithm_sets)
    new_initial = ""
    new_finals = []
    new_transitions = {}
    new_states = []

    for x in range(0, len(algorithm_sets)):
        new_states.append(str(x))
        new_transitions[str(x)] = {}
        for e in algorithm_sets[x]:
            if e == fa.initials:
                new_initial = str(x)
            if e in fa.finals:
                new_finals += str(x)
        for a in fa.alphabet:
            if e in equivalence.keys():
                new_transitions[str(x)][a] = equivalence[e][a]
    fa.initials = new_initial
    fa.finals = list(set(new_finals))
    fa.transitions = new_transitions
    fa.states = new_states


def determinize(fa):
    states = []
#    while len(states) != len(fa.transitions.keys()):
    states = [x for x in fa.transitions.keys()]
    for s in states:
        for k in fa.transitions[s].keys():
            st = fa.transitions[s][k]
            if st not in fa.states:
                fa.create_state2(st, False, False)
                each_state = st.split(", ")
                for e in each_state:
                    if e in fa.finals and st not in fa.finals:
                        fa.add_final2(st)
                    if e in fa.transitions.keys():
                        for a in fa.alphabet:
                            if a in fa.transitions[e].keys():
                                fa.create_transition2(st, fa.transitions[e][a], a)
    
    #verificar estados acessiveis
    acessiveis = set()
    acessiveis.add(fa.initials)
    aux_acessiveis = set()
    while acessiveis != aux_acessiveis:
        aux_acessiveis = {x for x in acessiveis} 
        for s in aux_acessiveis:
            for a in fa.transitions[s].keys():
                acessiveis.add(fa.transitions[s][a])
    
    states = [x for x in fa.states]
    for st in states:
        if st not in acessiveis:
            fa.delete_state2(st)
    
    #verificar estados mortos
    vivos = {x for x in fa.finals}
    aux_vivos = set()
    while vivos != aux_vivos:
        aux_vivos = {x for x in vivos}
        for s in fa.states:
            for a in fa.transitions[s].keys():
                if fa.transitions[s][a] in aux_vivos:
                    vivos.add(s)
    
    states = [x for x in fa.states]
    for st in states:
        if st not in vivos:
            fa.delete_state2(st)


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
