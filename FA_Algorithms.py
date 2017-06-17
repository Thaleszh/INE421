from Finite_Automata import Finite_Automata
#import pdb

def remove_unacess(fa):
    #verificar estados acessiveis
    acessiveis = set()
    acessiveis.add(fa.initials)
    aux_acessiveis = set()
    while acessiveis != aux_acessiveis:
        aux_acessiveis = {x for x in acessiveis} 
        for s in aux_acessiveis:
            for a in fa.transitions[s].keys():
                acessiveis.add(fa.transitions[s][a])
    #remover estados inacessiveis
    states = [x for x in fa.states]
    for st in states:
        if st not in acessiveis:
            fa.delete_state(st)

def remove_dead(fa):
    #verificar estados vivos
    vivos = {x for x in fa.finals}
    aux_vivos = set()
    while vivos != aux_vivos:
        aux_vivos = {x for x in vivos}
        for s in fa.states:
            for a in fa.transitions[s].keys():
                if fa.transitions[s][a] in aux_vivos:
                    vivos.add(s)
    #remover estados mortos
    states = [x for x in fa.states]
    for st in states:
        if st not in vivos:
            fa.delete_state(st)

def minimize(fa):
    
    remove_unacess(fa)
    remove_dead(fa)

    #-------------achar estados equivalentes------------

    #criar estado Fi e substituir indefinicoes por ele
    states = [x for x in fa.states]
    alphabet = [x for x in fa.alphabet]
    for s in states:
        for k in alphabet:
            if k not in fa.transitions[s].keys():
                fa.create_transition(s, "Fi", k)

    if "Fi" in fa.states:
        for k in fa.alphabet:
            fa.create_transition("Fi", "Fi", k)

    #criar conjuntos de equivalencia iniciais
    set_F = {x for x in fa.finals}
    set_KF = set()

    for s in fa.states:
        if s not in fa.finals:
            set_KF.add(s)

    algorithm_sets = [set_F, set_KF]
    aux_algorithm_sets = []

    if set_KF == set():
        algorithm_sets.remove(set_KF)

    #dicionario para comparacoes durante o algoritmo
    equivalence = {}
    
    #calcular conjuntos de equivalencia
    while algorithm_sets != aux_algorithm_sets:
        aux_algorithm_sets = [x for x in algorithm_sets]
        algorithm_sets = []

        #analisar cada conjunto de equivalencia
        for analysis_set in aux_algorithm_sets:
            #analisar cada estado dentro do conjunto e atualizar o dicionario de
            #equivalencia
            for state in analysis_set:
                equivalence[state] = {}
                for a in fa.alphabet:
                    for x in range(0, len(aux_algorithm_sets)):
                        if state in fa.transitions.keys():
                            if fa.transitions[state][a] in aux_algorithm_sets[x]:
                                equivalence[state][a] = str(x)
            
            #estados no analysis set
            keys = [x for x in analysis_set]
            aux_keys = [x for x in analysis_set]
            equivalent = False
            
            #baseado no dicionario equivalence, recalcular os conjuntos de
            #equivalencia
            while keys != []:
                analysing = keys.pop()
                algorithm_sets.append(set())
                algorithm_sets[-1].add(analysing)
                for k in aux_keys:
                    if k not in keys:
                        break
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
    
    #fim do while
    
    new_initial = ""
    new_finals = []
    new_transitions = {}
    new_states = []

    #baseado nos conjuntos de equivalencia, atualizar a fa
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


def epsilon_aux(fa):
    states = [x for x in fa.transitions.keys()]
    #print(states)
    for state in states:
        #pdb.set_trace()
        #print(state)
        if '&' in fa.transitions[state].keys():
            #calcular epsilon fecho
            o_state = fa.transitions[state]['&']
            #print(o_state)
            epsilon_f = state+", "+o_state
            while '&' in fa.transitions[o_state].keys():
                s_state = fa.transitions[o_state]['&']
                s_state_split = s_state.split(", ")
                for part in s_state_split:
                    if part not in epsilon_f:
                        epsilon_f = epsilon_f+", "+part
                o_state = s_state
            #print(epsilon_f)
            epsilon_f_split = epsilon_f.split(", ")
            #print(epsilon_f_split)
            fa.create_state(epsilon_f, False, False)
            for st in epsilon_f_split:
                if st in fa.finals:
                    fa.add_final(epsilon_f)
                    break
            if fa.initials == state:
                fa.add_initial(epsilon_f)
            #atualizar transicoes
            for k in fa.transitions.keys():
                for a in fa. transitions[k].keys():
                    if fa.transitions[k][a] == state:
                        fa.delete_transition(k, state, a)
                        fa.create_transition(k, epsilon_f, a)
            for s in epsilon_f_split:
                for a in fa.transitions[s].keys():
                    st_trans = fa.transitions[s][a]
                    fa.create_transition(epsilon_f, st_trans, a)

    #print(fa.transitions)
    #deletar transicoes por epsilon
    for k in fa.transitions.keys():
        if '&' in fa.transitions[k].keys():
            st_epsilon = fa.transitions[k]['&']
            fa.delete_transition(k, st_epsilon, '&')
                

def determinize_epsilon(fa):
    if '&' not in fa.alphabet:
        determinize(fa)
        return
    
    #calcule o epsilon fecho e atualizar estados
    epsilon_aux(fa)
    determinize(fa)

def determinize(fa):
    states = []
    #loop de determinizacao
    while len(states) != len(fa.transitions.keys()):
        states = [x for x in fa.transitions.keys()]
        for s in states:
            for k in fa.transitions[s].keys():
                st = fa.transitions[s][k]
                #caso o mesmo simbolo leve a mais de um estado
                #cria um novo estado equivalente
                if st not in fa.states:
                    fa.create_state(st, False, False)
                    each_state = st.split(", ")
                    for e in each_state:
                        if e in fa.finals and st not in fa.finals:
                            fa.add_final(st)
                        if e in fa.transitions.keys():
                            for a in fa.alphabet:
                                if a in fa.transitions[e].keys():
                                    fa.create_transition(st, fa.transitions[e][a], a)

    #remover estados inutilizados apos determinizacao
    remove_unacess(fa)
    remove_dead(fa)

def union(fa1, fa2):
    #criar novo automato
    fa3 = Finite_Automata()

    fa3.alphabet = fa1.alphabet + fa2.alphabet
    fa3.states = fa1.states + fa2.states
    fa3.finals = fa1.finals + fa2.finals
    
    #definir novo estado inicial que leva para os dois antigos
    #estados iniciais
    new_initial_final = False

    if fa1.initials in fa1.finals:
        new_initial_final = True
    if fa2.initials in fa2.finals:
        new_initial_final = True

    fa3.create_state(fa1.initials+", "+fa2.initials,
                      True, new_initial_final)
    
    for k in fa1.transitions[fa1.initials].keys():
        fa3.create_transition(fa3.initials, 
                              fa1.transitions[fa1.initials][k],
                              k)
    for k in fa2.transitions[fa2.initials].keys():
        fa3.create_transition(fa3.initials, 
                              fa2.transitions[fa2.initials][k],
                              k)
    for s in fa1.states:
        for k in fa1.transitions[s].keys():
            fa3.create_transition(s,fa1.transitions[s][k], k)

    for s in fa2.states:
        for k in fa2.transitions[s].keys():
            fa3.create_transition(s,fa2.transitions[s][k], k)

    determinize(fa3)
    return(fa3)

def complement(fa1):
    #criar novo automato
    fa2 = Finite_Automata()
    
    #inverter estados finais
    for s in fa1.states:
        fa2.create_state(s, False, False)
        if s not in fa1.finals:
            fa2.finals.append(s)
    
    fa2.initials = fa1.initials

    for k in fa1.transitions.keys():
        fa2.transitions[k] = {}
        for a in fa1.alphabet:
            fa2.transitions[k][a] = fa1.transitions[k][a]
    return fa2

def intersection(fa1, fa2):
    return complement(union(complement(fa1), complement(fa2)))

def dif(fa1, fa2):
    return intersection(fa1, complement(fa2))
