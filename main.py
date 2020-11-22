from state import State
from aialgorithms import alpha_star

limit = 30

family = {
    "George": 1,
    "Nick": 3,
    "Maria": 6,
    "Kostas": 8,
    "Lampros": 12
    }

initial_state = State(family)
terminal_state = alpha_star(initial_state, limit)
if terminal_state is not None:
    print("Yes!!!!")


