from state import State

states = []

def alphastar(initial_state, limit):
    global states
    states.append(initial_state)
    while states:
       current_state = states.pop(0)
       if current_state.is_terminal(limit):
           return current_state
       states.extend(current_state.get_children())
       states.sort(key = compare)
    return None



def compare(state):
    return state.get_score()