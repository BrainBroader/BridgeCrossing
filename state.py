class State:
    """ Represents an instance of the Bridge Crossing problem

    Attributes:
        start:
            A dictionary with the people and their crossing time at the starting side of the bridge
        finish:
            A dictionary with the people and their crossing time at the ending side of the bridge
        score:
            An integer representing the score of the state. Let n be the state, then the score is computed
            by the equation f(n) = h(n) + g(n), where h is the heuristic used and g is the cost from the root down to node n
        path:
            An integer representing the cost from the root down to this state
        father:
            A State object representing the predecessor of this state
    """

    def __init__(self, family, finish={}):
        self.start = family.copy()
        self.finish = finish.copy()
        self.score = -1
        self.path = 0
        self.father = None

    def cross_bridge(self, members):
        """ Transfers two people from the starting side to the finishing side of the bridge

        Args:
            members:
                A list with the names of those who will cross the bridge

        Returns:
            True if operation was successful, else False
        """
        if not self.start:
            return False

        self.finish[members[0]] = self.start.get(members[0])
        del self.start[members[0]]
        self.finish[members[1]] = self.start.get(members[1])
        del self.start[members[1]]

        return True

    def return_lamp(self, member):
        """ Transfers a person (holding the lamp) from the finishing side to the starting side of the bridge

        Args:
            member:
                The name of the person to return to the starting side of the bridge with the lamp

        Returns:
           True if operation was successful, else False
        """
        if not self.finish:
            return False

        self.start[member] = self.finish.get(member)
        del self.finish[member]

        return True

    def evaluate(self):
        """ Returns an integer representing the score of the state.

        The score is computed as follows: Let n be the state, then the score is computed by the equation
        f(n) = h(n) + g(n),
        where h is the heuristic used and g is the cost from the root down to node n

        Returns:
            The state's score as an integer
        """
        self.score = self.heuristic() + self.path_cost()
        return self.score

    def heuristic(self):
        """ Returns the estimated cost of the cheapest path from this state to a goal state

        The score produced by the heuristic is calculated by taking the maximum speed of
        all the people who are at the starting side of the bridge and still haven't crossed it

        Returns:
            The heuristic's score as an integer
        """
        if not self.start:
            return 0
        return max(self.start.values())

    # TODO
    def path_cost(self) -> int:
        # return self.father.path +
        pass

    # TODO
    def get_children(self):
        pass

    # TODO (?) use heuristic
    def is_terminal(self, limit):
        """ Checks if this state is a terminal state

        A state is considered to be terminal if its score has exceeded the time limitation
        or there aren't any more people in the starting side of the bridge

        Args:
            limit: time limitation of the Bridge Crossing game

        Returns:
            True if this is a terminal state, else False
        """
        if (self.score >= limit) or (not self.start):
            return True
        return False

    def get_start(self):
        return self.start

    def get_finish(self):
        return self.finish

    def get_score(self):
        return self.score

    def get_father(self):
        return self.father

    def set_start(self, start):
        self.start = start.copy()

    def set_finish(self, finish):
        self.finish = finish.copy()

    def set_score(self, score):
        self.score = score

    def set_father(self, father):
        self.father = father

    # FIXME override print operator ?
    def print(self):
        for i in self.start:
            print(i)
        print("-----------------------")
        for i in self.finish:
            print(i)
        print("-----------------------")
