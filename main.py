from Finite_Automata import Finite_Automata, State

def main():
    transitions = {"a": "q0"}
    final = True
    inicial = True
    nome = "q0"

    estado0 = State(nome, transitions, inicial, final)
    estado1 = State("q1", {"a" : "q0", "b" : "q0"}, False, True)
    estado2 = State("q2", {"a" : "q1", "b" : "q0"}, False, False)
   
    print(estado0.transitions)
    print(estado1.transitions)
    print(estado2.transitions)

    fa_estados = [estado0]
    fa1 = Finite_Automata(fa_estados)

    fa_estados2 = [estado2]
    fa2 = Finite_Automata(fa_estados2)
    
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)
'''
    print(1)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    fa1.create_state2("q1", {"a" : "q0"}, False, True)
    
    print("\n2")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    fa1.create_transition(estado0, estado1, "b")
    
    print("\n3")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    fa1.delete_transition(estado0, estado1, "b")

    print("\n4")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    print("\n5")
    fa1.delete_transition(estado2, estado1, "c")
    fa1.delete_transition(estado0, estado1, "c")
    fa1.delete_transition(estado0, estado1, "a")

    fa1.delete_state(estado0)

    print("\n6")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    fa1.create_state1(estado2)
    fa1.create_state1(estado0)

    print("\n7")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    print("\n8")
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)

    fa2.create_transition(estado0, estado2, "b")

    print("\n9")
    print(fa2.transitions)
    print(fa2.initials)
    print(fa2.finals)

    print("\n10")
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)
'''
main()
