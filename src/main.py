import sys

from filehandler import read_csv

from state import State
from aialgorithms import alpha_star

if len(sys.argv) != 3:
    print("[ERROR] main - Missing command line arguments")
    print("[ERROR] main - First argument must be a valid path to the dataset")
    print("[ERROR] main - Second argument must be zero or a positive integer")
    sys.exit(1)

print("[INFO] main - Loading CSV file from " + sys.argv[1] + "...\n")
people = read_csv(sys.argv[1])
if people is None:
    print("[ERROR] main - First argument must be a valid path")
    sys.exit(1)

limit = 0
try:
    limit = int(sys.argv[2])
    if limit < 0:
        raise ValueError
except ValueError:
    print("[ERROR] main - Second argument must be zero or a positive integer")
    sys.exit(1)

print("[INFO] main - Calculating solution...\n")

initial_state = State(people)
terminal_state = alpha_star(initial_state, limit)

if terminal_state is not None:
    if limit > 0:
        if terminal_state.get_score() > limit:
            print("[INFO] main - Solution not found, due to exceeded time limit.")
        else:
            print("[INFO] main - The family crossed the bridge in " + str(terminal_state.get_score()) + " seconds.")
            print("[INFO] main - The path found by A* algorithm is as follows:")
            temp = terminal_state
            path = [terminal_state]
            while temp.get_father() is not None:
                path.append(temp.get_father())
                temp = temp.get_father()
            [x.print() for x in path[::-1]]
    elif limit == 0:
        print("[INFO] main - The family crossed the bridge in " + str(terminal_state.get_score()) + " seconds.")
        print("[INFO] main - The path found by A* algorithm is as follows:")
        temp = terminal_state
        path = [terminal_state]
        while temp.get_father() is not None:
            path.append(temp.get_father())
            temp = temp.get_father()
        [x.print() for x in path[::-1]]



