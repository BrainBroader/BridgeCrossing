from state import State

family = {
    "george": 15,
    "nick": 20,
    "maria": 10,
    "kostas": 15
    }

f1 = State(family)
#f1.print()
f1.evaluate()
f1.cross_bridge(("george", "nick"))
f1.print()
f1.return_lamp("nick")
f1.print()
print(f1.heuristic())
if {}:
    print("hello")

