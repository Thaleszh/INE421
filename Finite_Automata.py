

class Finite_Automata(object):
  def __init__(self, states):
    #	[transition, final, initial]
    #	Example state: 
    #	q0 = [[a : q2, b : q3], false, true]
    #
    self.fa_data = {}
    for state in states:
      self.fa_data[state] = [state.getTransitions(), state.getFinal(), state.getInitial()]
