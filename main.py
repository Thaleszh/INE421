from FA_Algorithms import determinize, minimize, complement, union
from Finite_Automata import Finite_Automata, State
import pdb


def main():
    
    fa_div_3 = Finite_Automata()
    fa_div_3.create_state("0", True, True)
    fa_div_3.create_state("1", False, False)
    fa_div_3.create_state("2", False, False)

    fa_div_3.create_transition("0", "0", '0')
    fa_div_3.create_transition("0", "1", '1')
    fa_div_3.create_transition("1", "2", '0')
    fa_div_3.create_transition("1", "0", '1')
    fa_div_3.create_transition("2", "1", '0')
    fa_div_3.create_transition("2", "2", '1')

    fa_div_2 = Finite_Automata()
    fa_div_2.create_state("3", True, True)
    fa_div_2.create_state("4", False, False)

    fa_div_2.create_transition("3", "3", '0')
    fa_div_2.create_transition("3", "4", '1')
    fa_div_2.create_transition("4", "3", '0')
    fa_div_2.create_transition("4", "4", '1')

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
    fa_div_3.create_state("0", True, True)
    fa_div_3.create_state("1", False, False)
    fa_div_3.create_state("2", False, False)

    fa_div_3.create_transition("0", "0", '0')
    fa_div_3.create_transition("0", "1", '1')
    fa_div_3.create_transition("1", "2", '0')
    fa_div_3.create_transition("1", "0", '1')
    fa_div_3.create_transition("2", "1", '0')
    fa_div_3.create_transition("2", "2", '1')

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
    fa_no_determinize.create_state("S", True, False)
    fa_no_determinize.create_state("A", False, False)
    fa_no_determinize.create_state("B", False, True)

    fa_no_determinize.create_transition("S", "S", '0')
    fa_no_determinize.create_transition("S", "S", '1')
    fa_no_determinize.create_transition("S", "A", '1')
    fa_no_determinize.create_transition("A", "B", '0')
    fa_no_determinize.create_transition("A", "B", '1')

    print(fa_no_determinize.transitions)

    determinize(fa_no_determinize)
    
    print(fa_no_determinize.states)
    print(fa_no_determinize.finals)
    print(fa_no_determinize.initials)
    print(fa_no_determinize.transitions)
    
'''
'''
    fa_not_min = Finite_Automata()
    fa_not_min.create_state("I", True, True)
    fa_not_min.create_state("S", False, True)
    fa_not_min.create_state("A", False, False)
    fa_not_min.create_state("C", False, False)
    fa_not_min.create_state("D", False, True)
    fa_not_min.create_state("E", False, True)

    fa_not_min.create_transition("I", "A", 'a')
    fa_not_min.create_transition("I", "A", 'b')
    fa_not_min.create_transition("I", "C", 'b')
    fa_not_min.create_transition("I", "C", 'c')

    fa_not_min.create_transition("S", "A", 'a')
    fa_not_min.create_transition("S", "A", 'b')
    fa_not_min.create_transition("S", "C", 'b')
    fa_not_min.create_transition("S", "C", 'c')

    fa_not_min.create_transition("A", "S", 'b')
    fa_not_min.create_transition("A", "D", 'c')
    
    fa_not_min.create_transition("C", "E", 'a')
    fa_not_min.create_transition("C", "S", 'b')
    
    fa_not_min.create_transition("D", "A", 'a')
    fa_not_min.create_transition("D", "A", 'b')
    fa_not_min.create_transition("D", "C", 'b')

    fa_not_min.create_transition("E", "A", 'b')
    fa_not_min.create_transition("E", "C", 'b')
    fa_not_min.create_transition("E", "C", 'c')
    
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
    fa_not_min.create_state("S", True, True)
    fa_not_min.create_state("A", False, False)
    fa_not_min.create_state("B", False, True)
    fa_not_min.create_state("C", False, True)
    fa_not_min.create_state("D", False, False)

    fa_not_min.create_transition("S", "B", 'a')
    fa_not_min.create_transition("S", "D", 'a')
    fa_not_min.create_transition("S", "A", 'b')
    fa_not_min.create_transition("S", "C", 'b')

    fa_not_min.create_transition("A", "B", 'a')
    fa_not_min.create_transition("A", "A", 'b')
    
    fa_not_min.create_transition("B", "A", 'a')
    fa_not_min.create_transition("B", "B", 'b')
    
    fa_not_min.create_transition("C", "D", 'a')
    fa_not_min.create_transition("C", "C", 'b')
    
    fa_not_min.create_transition("D", "C", 'a')
    fa_not_min.create_transition("D", "D", 'b')

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

    fa1.create_state("q0", True, True)
    fa1.create_state("q1", False, True)
    fa1.create_state("q2", False, False)

    fa2.create_state("S", True, False)
    fa2.create_state("A", False, False)
    fa2.create_state("B", False, True)


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

    fa2.create_transition("S", "A", "a")
    fa2.create_transition("A", "B", "b")
    fa2.create_transition("B", "S", "c")
    fa2.create_transition("B", "A", "a")
    fa2.create_transition("B", "B", "a")
    
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
            fa1.create_transition(t, fa2.transitions[t][k], k)

    print(fa1.transitions)

    print("\n3")

    fa2.create_transition("S", "D", "d")

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

    fa2.delete_transition("S", "D", "d")

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

    fa2.delete_state("A")

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

    fa2.delete_state("C")

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
