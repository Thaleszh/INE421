from FA_Algorithms import determinize, minimize, complement, union, dif
from FA_Algorithms import determinize_epsilon, equivalence
from RE_Algorithms import de_simone
from Finite_Automata import Finite_Automata
#import pdb


def main():

    fa1 = Finite_Automata()
    
    fa1.create_state("S", True, True) 
    fa1.create_state("A", False, False) 
    
    fa1.create_transition("S", "A", 'a')
    fa1.create_transition("S", "S", 'b')
    fa1.create_transition("A", "S", 'a')
    fa1.create_transition("A", "A", 'b')

    print('FA 1')
    print('a')
    print(fa1.alphabet)
    print('sts')
    print(fa1.states)
    print('f')
    print(fa1.finals)
    print('i')
    print(fa1.initials)
    print('t')
    print(fa1.transitions)
    print('\n')
    
    fa2 = Finite_Automata()

    fa2.create_state("Z", True, True) 
    fa2.create_state("B", False, True) 
    
    fa2.create_transition("Z", "B", 'a')
    fa2.create_transition("Z", "Z", 'b')
    fa2.create_transition("B", "Z", 'b')
    
    print('FA 2')
    print('a')
    print(fa2.alphabet)
    print('sts')
    print(fa2.states)
    print('f')
    print(fa2.finals)
    print('i')
    print(fa2.initials)
    print('t')
    print(fa2.transitions)
    print('\n')
    

    fa3 = union(fa1, fa2)
    print('FA 3')
    print('a')
    print(fa3.alphabet)
    print('sts')
    print(fa3.states)
    print('f')
    print(fa3.finals)
    print('i')
    print(fa3.initials)
    print('t')
    print(fa3.transitions)
    print('\n')
    
'''
    fa2 = Finite_Automata()
    
    fa2.create_state("A", True, True)
    fa2.create_state("B", False, False)
    fa2.create_state("C", False, False)
    fa2.create_state("D", False, True)
    fa2.create_state("E", False, False)
    fa2.create_state("F", False, False)
    fa2.create_state("G", False, True)
    fa2.create_state("H", False, False)

    fa2.create_transition("A", "G", 'a')
    fa2.create_transition("A", "B", 'b')
    fa2.create_transition("B", "F", 'a')
    fa2.create_transition("B", "E", 'b')
    fa2.create_transition("C", "C", 'a')
    fa2.create_transition("C", "G", 'b')
    fa2.create_transition("D", "A", 'a')
    fa2.create_transition("D", "H", 'b')
    fa2.create_transition("E", "E", 'a')
    fa2.create_transition("E", "A", 'b')
    fa2.create_transition("F", "B", 'a')
    fa2.create_transition("F", "C", 'b')
    fa2.create_transition("G", "G", 'a')
    fa2.create_transition("G", "F", 'b')
    fa2.create_transition("H", "H", 'a')
    fa2.create_transition("H", "D", 'b')

    print('FA 2')
    print('a')
    print(fa2.alphabet)
    print('sts')
    print(fa2.states)
    print('f')
    print(fa2.finals)
    print('i')
    print(fa2.initials)
    print('t')
    print(fa2.transitions)
    print('\n')
    
    minimize(fa2)
    print('FA 2')
    print('a')
    print(fa2.alphabet)
    print('sts')
    print(fa2.states)
    print('f')
    print(fa2.finals)
    print('i')
    print(fa2.initials)
    print('t')
    print(fa2.transitions)
    print('\n')
'''
'''
    fa1 = Finite_Automata()

    fa1.create_state("q0", True, False)
    fa1.create_state("q1", False, False)
    fa1.create_state("q2", False, True)
    fa1.create_state("q3", False, False)
    fa1.create_state("q4", False, True)

    fa1.create_transition("q0", "q0", '0')
    fa1.create_transition("q0", "q0", '1')
    fa1.create_transition("q0", "q1", '0')
    fa1.create_transition("q0", "q3", '1')
    fa1.create_transition("q1", "q2", '0')
    fa1.create_transition("q2", "q2", '0')
    fa1.create_transition("q2", "q2", '1')
    fa1.create_transition("q3", "q4", '1')
    fa1.create_transition("q4", "q4", '0')
    fa1.create_transition("q4", "q4", '1')

    print('FA 1')
    print('a')
    print(fa1.alphabet)
    print('sts')
    print(fa1.states)
    print('f')
    print(fa1.finals)
    print('i')
    print(fa1.initials)
    print('t')
    print(fa1.transitions)
    print('\n')

    determinize(fa1)
    print('FA 1')
    print('a')
    print(fa1.alphabet)
    print('sts')
    print(fa1.states)
    print('f')
    print(fa1.finals)
    print('i')
    print(fa1.initials)
    print('t')
    print(fa1.transitions)
    print('\n')

'''
'''
    fa1 = Finite_Automata()

    fa1.create_state("S", True, True)
    fa1.create_state("A, B", False, False)

    fa1.create_transition("S", "A, B", 'a')
    #fa1.create_transition("S", "S", 'b')
    fa1.create_transition("A, B", "S", 'a')
    fa1.create_transition("A, B", "A, B", 'b')

    print('FA 1')
    print('a')
    print(fa1.alphabet)
    print('sts')
    print(fa1.states)
    print('f')
    print(fa1.finals)
    print('i')
    print(fa1.initials)
    print('t')
    print(fa1.transitions)
    print('\n')
    
    fa1.create_transition("S", "B, A", 'b')
    fa1.create_transition("S", "A, B, B", 'b')

    print('FA 1')
    print('a')
    print(fa1.alphabet)
    print('sts')
    print(fa1.states)
    print('f')
    print(fa1.finals)
    print('i')
    print(fa1.initials)
    print('t')
    print(fa1.transitions)
    print('\n')

'''    
'''
    fa_test1 = de_simone("a|m")
    fa_test2 = de_simone("m|a")


    print('FA 1')
    print(fa_test1.alphabet)
    print(fa_test1.states)
    print(fa_test1.finals)
    print(fa_test1.initials)
    print(fa_test1.transitions)
    print('\n')
    print('FA 2')
    print(fa_test2.alphabet)
    print(fa_test2.states)
    print(fa_test2.finals)
    print(fa_test2.initials)
    print(fa_test2.transitions)
    print('\n')

    fa_test3 = union(fa_test1, fa_test2)
    print('FA 3')
    print(fa_test3.alphabet)
    print(fa_test3.states)
    print(fa_test3.finals)
    print(fa_test3.initials)
    print(fa_test3.transitions)
    print('\n')
'''
'''    
    fa_test1 = Finite_Automata()
    fa_test1.create_state("s0", True, False)
    fa_test1.create_state("s1", False, True)

    fa_test1.create_transition("s0", "s1", 'a')
    fa_test1.create_transition("s0", "s0", 'b')
    fa_test1.create_transition("s1", "s1", 'a')
    fa_test1.create_transition("s1", "s1", 'b')
    
    print('FA 1')
    print(fa_test1.alphabet)
    print(fa_test1.states)
    print(fa_test1.finals)
    print(fa_test1.initials)
    print(fa_test1.transitions)
    print('\n')

    fa_test2 = Finite_Automata()
    fa_test2.create_state("q0", True, False)
    fa_test2.create_state("q1", False, True)

    fa_test2.create_transition("q0", "q1", 'a')
    fa_test2.create_transition("q0", "q1", 'b')
    fa_test2.create_transition("q1", "q1", 'a')
    fa_test2.create_transition("q1", "q1", 'b')
    
    print('FA 2')
    print(fa_test2.alphabet)
    print(fa_test2.states)
    print(fa_test2.finals)
    print(fa_test2.initials)
    print(fa_test2.transitions)
    print('\n')

    print(equivalence(fa_test2, fa_test1))
'''
'''
    fa_test1 = Finite_Automata()
    fa_test1.create_state("s0", True, False)
    fa_test1.create_state("s1", False, True)

    fa_test1.create_transition("s0", "s1", 'a')
    fa_test1.create_transition("s0", "s1", 'b')
    fa_test1.create_transition("s0", "s0", 'c')
    fa_test1.create_transition("s1", "s1", 'a')
    fa_test1.create_transition("s1", "s1", 'b')
    fa_test1.create_transition("s1", "s0", 'c')
    
    print('FA 1')
    print(fa_test1.alphabet)
    print(fa_test1.states)
    print(fa_test1.finals)
    print(fa_test1.initials)
    print(fa_test1.transitions)
    print('\n')

    fa_test2 = Finite_Automata()
    fa_test2.create_state("q0", True, True)
    fa_test2.create_state("q1", False, False)

    fa_test2.create_transition("q0", "q1", 'a')
    fa_test2.create_transition("q0", "q0", 'b')
    fa_test2.create_transition("q1", "q0", 'a')
    fa_test2.create_transition("q1", "q1", 'b')
    
    print('FA 2')
    print(fa_test2.alphabet)
    print(fa_test2.states)
    print(fa_test2.finals)
    print(fa_test2.initials)
    print(fa_test2.transitions)
    print('\n')

    not_fa_test1 = complement(fa_test1)
    not_fa_test2 = complement(fa_test2)

    print('not FA1')
    print(not_fa_test1.alphabet)
    print(not_fa_test1.states)
    print(not_fa_test1.finals)
    print(not_fa_test1.initials)
    print(not_fa_test1.transitions)
    print('not FA2')
    print(not_fa_test2.alphabet)
    print(not_fa_test2.states)
    print(not_fa_test2.finals)
    print(not_fa_test2.initials)
    print(not_fa_test2.transitions)
    print('\n')

    union_not = complement(union(not_fa_test1, fa_test2))
    print('Union not')
    print(union_not.alphabet)
    print(union_not.states)
    print(union_not.finals)
    print(union_not.initials)
    print(union_not.transitions)
    print('\n')

    fa_test3 = dif(fa_test1, fa_test2)

    print('FA 3')
    print(fa_test3.alphabet)
    print(fa_test3.states)
    print(fa_test3.finals)
    print(fa_test3.initials)
    print(fa_test3.transitions)
    print('\n')
'''
'''    
    fa_test = Finite_Automata()
    fa_test.create_state("0", True, False)
    fa_test.create_state("1", False, False)
    fa_test.create_state("2", False, True)

    fa_test.create_transition("0", "0", 'a')
    fa_test.create_transition("0", "1", 'b')
    fa_test.create_transition("0", "2", 'b')
    fa_test.create_transition("1", "1", 'a')
    fa_test.create_transition("1", "2", 'b')
    fa_test.create_transition("2", "2", 'a')
    fa_test.create_transition("2", "2", 'b')
    
    print(fa_test.alphabet)
    print(fa_test.states)
    print(fa_test.finals)
    print(fa_test.initials)
    print(fa_test.transitions)

    fa_test.delete_all_transitions("0", 'b')
    
    print(fa_test.alphabet)
    print(fa_test.states)
    print(fa_test.finals)
    print(fa_test.initials)
    print(fa_test.transitions)
''' 
'''
    fa_epsilon = Finite_Automata()
    fa_epsilon.create_state("0", True, False)
    fa_epsilon.create_state("1", False, False)
    fa_epsilon.create_state("2", False, True)

    fa_epsilon.create_transition("0", "0", 'a')
    fa_epsilon.create_transition("0", "1", 'b')
    fa_epsilon.create_transition("0", "1", '&')
    fa_epsilon.create_transition("1", "1", 'a')
    fa_epsilon.create_transition("1", "2", 'b')
    #fa_epsilon.create_transition("1", "2", '&')
    fa_epsilon.create_transition("2", "2", 'a')
    fa_epsilon.create_transition("2", "2", 'b')
    
    print('epsilon')
    print(fa_epsilon.alphabet)
    print(fa_epsilon.states)
    print(fa_epsilon.finals)
    print(fa_epsilon.initials)
    print(fa_epsilon.transitions)

    determinize_epsilon(fa_epsilon)

    print('nao-epsilon')
    print(fa_epsilon.alphabet)
    print(fa_epsilon.states)
    print(fa_epsilon.finals)
    print(fa_epsilon.initials)
    print(fa_epsilon.transitions)
'''
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
