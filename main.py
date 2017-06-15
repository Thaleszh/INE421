from FA_Algorithms import determinize, minimize, complement, union
from Finite_Automata import Finite_Automata, State
import pdb


def main():
    
    fa_div_3 = Finite_Automata()
    fa_div_3.create_state2("0", True, True)
    fa_div_3.create_state2("1", False, False)
    fa_div_3.create_state2("2", False, False)

    fa_div_3.create_transition2("0", "0", '0')
    fa_div_3.create_transition2("0", "1", '1')
    fa_div_3.create_transition2("1", "2", '0')
    fa_div_3.create_transition2("1", "0", '1')
    fa_div_3.create_transition2("2", "1", '0')
    fa_div_3.create_transition2("2", "2", '1')

    fa_div_2 = Finite_Automata()
    fa_div_2.create_state2("3", True, True)
    fa_div_2.create_state2("4", False, False)

    fa_div_2.create_transition2("3", "3", '0')
    fa_div_2.create_transition2("3", "4", '1')
    fa_div_2.create_transition2("4", "3", '0')
    fa_div_2.create_transition2("4", "4", '1')

    print('div3')
    print(fa_div_3.states)
    print(fa_div_3.finals)
    print(fa_div_3.initials)
    print(fa_div_3.transitions)

    print('div2')
    print(fa_div_2.states)
    print(fa_div_2.finals)
    print(fa_div_2.initials)
    print(fa_div_2.transitions)
    
    union_fa = union(fa_div_2, fa_div_3) 
    
    print('union')
    print(union_fa.states)
    print(union_fa.finals)
    print(union_fa.initials)
    print(union_fa.transitions)
'''    
    fa_div_3 = Finite_Automata()
    fa_div_3.create_state2("0", True, True)
    fa_div_3.create_state2("1", False, False)
    fa_div_3.create_state2("2", False, False)

    fa_div_3.create_transition2("0", "0", '0')
    fa_div_3.create_transition2("0", "1", '1')
    fa_div_3.create_transition2("1", "2", '0')
    fa_div_3.create_transition2("1", "0", '1')
    fa_div_3.create_transition2("2", "1", '0')
    fa_div_3.create_transition2("2", "2", '1')

    print(fa_div_3.states)
    print(fa_div_3.finals)
    print(fa_div_3.initials)
    print(fa_div_3.transitions)

    fa_not_div_3 = complement(fa_div_3)

    print(fa_not_div_3.states)
    print(fa_not_div_3.finals)
    print(fa_not_div_3.initials)
    print(fa_not_div_3.transitions)
'''
'''   
    fa_no_determinize = Finite_Automata()
    fa_no_determinize.create_state2("S", True, False)
    fa_no_determinize.create_state2("A", False, False)
    fa_no_determinize.create_state2("B", False, True)

    fa_no_determinize.create_transition2("S", "S", '0')
    fa_no_determinize.create_transition2("S", "S", '1')
    fa_no_determinize.create_transition2("S", "A", '1')
    fa_no_determinize.create_transition2("A", "B", '0')
    fa_no_determinize.create_transition2("A", "B", '1')

    print(fa_no_determinize.transitions)

    determinize(fa_no_determinize)
    
    print(fa_no_determinize.states)
    print(fa_no_determinize.finals)
    print(fa_no_determinize.initials)
    print(fa_no_determinize.transitions)
    
'''
'''
    fa_not_min = Finite_Automata()
    fa_not_min.create_state2("I", True, True)
    fa_not_min.create_state2("S", False, True)
    fa_not_min.create_state2("A", False, False)
    fa_not_min.create_state2("C", False, False)
    fa_not_min.create_state2("D", False, True)
    fa_not_min.create_state2("E", False, True)

    fa_not_min.create_transition2("I", "A", 'a')
    fa_not_min.create_transition2("I", "A", 'b')
    fa_not_min.create_transition2("I", "C", 'b')
    fa_not_min.create_transition2("I", "C", 'c')

    fa_not_min.create_transition2("S", "A", 'a')
    fa_not_min.create_transition2("S", "A", 'b')
    fa_not_min.create_transition2("S", "C", 'b')
    fa_not_min.create_transition2("S", "C", 'c')

    fa_not_min.create_transition2("A", "S", 'b')
    fa_not_min.create_transition2("A", "D", 'c')
    
    fa_not_min.create_transition2("C", "E", 'a')
    fa_not_min.create_transition2("C", "S", 'b')
    
    fa_not_min.create_transition2("D", "A", 'a')
    fa_not_min.create_transition2("D", "A", 'b')
    fa_not_min.create_transition2("D", "C", 'b')

    fa_not_min.create_transition2("E", "A", 'b')
    fa_not_min.create_transition2("E", "C", 'b')
    fa_not_min.create_transition2("E", "C", 'c')
    
    print('1')
    print(fa_not_min.alphabet)
    print(fa_not_min.states)
    print(fa_not_min.finals)
    print(fa_not_min.initials)
    print(fa_not_min.transitions)
    print('\n')
    
    determinize(fa_not_min)

    print('2')
    print(fa_not_min.alphabet)
    print(fa_not_min.states)
    print(fa_not_min.transitions)
    print('\n')

    minimize(fa_not_min)
    
    print('3')
    print(fa_not_min.transitions)
    print(fa_not_min.states)
    print(fa_not_min.finals)
    print(fa_not_min.initials)
    print('\n')
'''
'''
    fa_not_min = Finite_Automata()
    fa_not_min.create_state2("S", True, True)
    fa_not_min.create_state2("A", False, False)
    fa_not_min.create_state2("B", False, True)
    fa_not_min.create_state2("C", False, True)
    fa_not_min.create_state2("D", False, False)

    fa_not_min.create_transition2("S", "B", 'a')
    fa_not_min.create_transition2("S", "D", 'a')
    fa_not_min.create_transition2("S", "A", 'b')
    fa_not_min.create_transition2("S", "C", 'b')

    fa_not_min.create_transition2("A", "B", 'a')
    fa_not_min.create_transition2("A", "A", 'b')
    
    fa_not_min.create_transition2("B", "A", 'a')
    fa_not_min.create_transition2("B", "B", 'b')
    
    fa_not_min.create_transition2("C", "D", 'a')
    fa_not_min.create_transition2("C", "C", 'b')
    
    fa_not_min.create_transition2("D", "C", 'a')
    fa_not_min.create_transition2("D", "D", 'b')

    print('1')
    print(fa_not_min.alphabet)
    print(fa_not_min.states)
    print(fa_not_min.finals)
    print(fa_not_min.initials)
    print(fa_not_min.transitions)
    print('\n')
    
    determinize(fa_not_min)

    print('2')
    print(fa_not_min.alphabet)
    print(fa_not_min.states)
    print(fa_not_min.transitions)
    print('\n')

    minimize(fa_not_min)
    
    print('3')
    print(fa_not_min.transitions)
    print(fa_not_min.states)
    print(fa_not_min.finals)
    print(fa_not_min.initials)
    print('\n')


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
