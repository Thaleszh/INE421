from Finite_Automata import Finite_Automata, State

def main():
    transitions = {"a": "q0"}
    final = True
    inicial = True
    nome = "q0"

    estado0 = State(nome, transitions, inicial, final)
    estado1 = State("q1", {"a" : "q0", "b" : "q0"}, False, True)
    estado2 = State("q2", {"a" : "q1", "b" : "q0"}, False, False)
    
    fa_estados = [estado0]

    fa1 = Finite_Automata(fa_estados)

    print(1)
    print(fa1.transitions)
    print(fa1.initials)
    print(fa1.finals)

    fa1.create_state("q1", {"a" : "q0"}, False, True)
    
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

main()
