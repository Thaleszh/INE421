import Finite_Automata

def minimize(fa):
    all_states = set(x for x in fa.transitions.keys())
    
    #verificar estados acessiveis
    acessiveis = set(x for x in fa.initials)
   

    while acessiveis != new_acessiveis:
        new_acessiveis = acessiveis
        for s in acessiveis:
            for a in fa.transitions[s].keys():
                new_acessiveis.add(fa.transitions[s][a])

    for state in all_states not in acessiveis:
        fa.delete_state(state)

    #verificar estados mortos
    vivos = set(x for x in fa.finals)

    while vivos != new_vivos:
        new_vivos = vivos
        for state in vivos
            for s in all_states
                for a in fa.transitions[s].keys():
                    if fa.transitions[s][a] is state.name
                        new_vivos.add(s)

    for state in all_states not in vivos:
        fa.delete_state(state)

    #achar estados equivalentes
    

def determinize(fa):
    pass

def union(fa1, fa2):
    pass

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
