""" A module containing AI algorithms for searching.

TODO reference the algorithms included
"""

from state import State


def alpha_star(initial_state, limit):
    """ An implementation of Alpha Star algorithm.

    Args:
        initial_state: A State object representing the state from which search will start.
        limit: An int representing the time limit of search.

    Returns:
       A State object representing the goal-state.
    """
    states = [initial_state]
    while states:
        current_state = states.pop(0)
        if current_state.is_terminal(limit):
            return current_state
        states.extend(current_state.get_children())
        states.sort(key=State.compare)
    return None
