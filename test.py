from state import State
from aialgorithms import alpha_star

limit = 30

family = {
    "george": 1,
    "nick": 3,
    "maria": 6,
    "kostas": 8,
    "lampros": 12
    }



terminal_state = None
initial_state = State(family)
terminal_state = alpha_star.alphastar(initial_state, limit)
if terminal_state is not None:
    print("Yes!!!!")


