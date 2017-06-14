from FA_Algorithms import determinize, minimize
from Finite_Automata import Finite_Automata, State

def main():

    fa_not_min = Finite_Automata()
    fa_not_min.create_state2("S", True, False)
    fa_not_min.create_state2("A", False, False)
    fa_not_min.create_state2("B", False, True)
    fa_not_min.create_state2("M1", False, False)
    fa_not_min.create_state2("M2", False, False)

    fa_not_min.create_transition2("S", "S", '0')
    fa_not_min.create_transition2("S", "A", '1')
    fa_not_min.create_transition2("A", "B", '0')
    fa_not_min.create_transition2("A", "B", '1')
    fa_not_min.create_transition2("M1", "M1", '0')
    fa_not_min.create_transition2("M1", "M1", '1')
    fa_not_min.create_transition2("B", "B", '0')
    fa_not_min.create_transition2("B", "M2", '1')
    fa_not_min.create_transition2("M2", "M2", '0')
    fa_not_min.create_transition2("M2", "M2", '1')

    print(fa_not_min.transitions)

    minimize(fa_not_min)

    print(fa_not_min.transitions)
    
'''
    fa_no_determinize = Finite_Automata()
    fa_no_determinize.create_state2("S", True, False)
    fa_no_determinize.create_state2("A", False, False)
    fa_no_determinize.create_state2("B", False, False)

    fa_no_determinize.create_transition2("S", "S", '0')
    fa_no_determinize.create_transition2("S", "S", '1')
    fa_no_determinize.create_transition2("S", "A", '1')
    fa_no_determinize.create_transition2("A", "B", '0')
    fa_no_determinize.create_transition2("A", "B", '1')

    print(fa_no_determinize.transitions)

    determinize(fa_no_determinize)
    fa_determinize = fa_no_determinize 

    print(fa_determinize.transitions)
''' 
    
'''   
    final = True
    inicial = True
    nome = "q0"

    estado0 = State(nome, inicial, final)
    estado1 = State("q1", False, True)
    estado2 = State("q2", False, False)
    estado3 = State("q3", False, False)

    fa1 = Finite_Automata()

    fa2 = Finite_Automata()
    
    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)

    print("\n1")

    fa1.create_state1(estado0)
    fa1.create_state1(estado1)
    fa1.create_state1(estado2)

    fa2.create_state2("S", True, False)
    fa2.create_state2("A", False, False)
    fa2.create_state2("B", False, True)


    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)


    print("\n2")

    fa1.create_transition1(estado0, estado1, "a")
    fa1.create_transition1(estado1, estado2, "b")
    fa1.create_transition1(estado2, estado0, "c")
    fa2.create_transition2("S", "A", "a")
    fa2.create_transition2("A", "B", "b")
    fa2.create_transition2("B", "S", "c")
    fa2.create_transition2("B", "A", "a")
    fa2.create_transition2("B", "B", "a")
    
    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)

    for t in fa2.states:
        for k in fa2.transitions[t].keys():
            fa1.create_transition2(t, fa2.transitions[t][k], k)

    print(fa1.transitions)

    print("\n3")

    fa1.create_transition1(estado0, estado3, "b")
    fa2.create_transition2("S", "D", "d")

    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)


    print("\n4")

    fa1.delete_transition1(estado0, estado3, "b")
    fa2.delete_transition2("S", "D", "d")

    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)


    print("\n5")

    fa1.delete_state1(estado2)
    fa2.delete_state2("A")

    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)


    print("\n6")

    fa1.delete_state1(estado2)
    fa2.delete_state2("C")

    print("fa1")
    print(fa1.states)
    print(fa1.alphabet)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print("fa2")
    print(fa2.states)
    print(fa2.alphabet)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)
'''
main()
