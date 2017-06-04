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

    set_F = set(x for x in fa.finals)
    set_KF = set(x for x in fa.states not in finals}

    for s in set_F:
############################

def determinize(fa):
    pass

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
