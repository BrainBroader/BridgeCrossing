import sys

from filehandler import read_csv

from state import State
from aialgorithms import alpha_star

people = read_csv(sys.argv[1])
limit = int(sys.argv[2])

initial_state = State(people)
terminal_state = alpha_star(initial_state, limit)

if terminal_state is not None:
    print("Yes!!!!")


