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
            fa.create_transition(s, "Fi", k)

    set_F = set(x for x in fa.finals)
    set_KF = set(x for x in fa.states not in finals}

    for s in set_F:


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
