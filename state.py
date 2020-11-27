from itertools import combinations


class State:
    """ Represents an instance of the Bridge Crossing problem

    Attributes:
        start:
            A dictionary with the people and their crossing time at the starting side of the bridge.
        finish:
            A dictionary with the people and their crossing time at the finishing side of the bridge.
        lamp:
            A boolean that indicates whether the lamp has returned at the starting side of the bridge.
            If True, then the next move must be the crossing of two people to the finishing side. Else, one person must
            return with the lamp at the starting side of the bridge.
        score:
            An integer representing the score of the state. Let n be the state, then the score is computed
            by the equation f(n) = h(n) + g(n), where h is the heuristic used and g is the cost from the root down to node n.
        path:
            An integer representing the cost from the root down to this state.
        cost_state:
            An integer representing the cost of this state. If the possible move is the crossing of the bridge
            towards the finishing side, then the cost is equal to the maximum time of the people. Else, if the possible
            move is the return of the lamp to the starting side, the cost is equal to the time of the person carrying it.
        father:
            A State object representing the predecessor of this state.
    """

    def __init__(self, family, finish={}):
        self.start = family.copy()
        self.finish = finish.copy()
        self.lamp = True
        self.score = -1
        self.path = 0
        self.cost_state = -1
        self.father = None

    def cross_bridge(self, people):
        """ Transfers two people from the starting side to the finishing side of the bridge.

        Args:
            people:
                A list with the names of those who will cross the bridge.

        Returns:
            True if operation was successful, else False.
        """
        if not self.start:
            return False

        self.finish[people[0]] = self.start.get(people[0])
        del self.start[people[0]]
        self.finish[people[1]] = self.start.get(people[1])
        del self.start[people[1]]
        self.cost_state = max(self.finish.get(people[0]), self.finish.get(people[1]))
        self.lamp = False

        return True

    def return_lamp(self, member):
        """ Transfers a person (holding the lamp) from the finishing side to the starting side of the bridge.

        Args:
            member:
                The name of the person to return to the starting side of the bridge with the lamp.

        Returns:
           True if operation was successful, else False.
        """
        if not self.finish:
            return False

        self.start[member] = self.finish.get(member)
        del self.finish[member]
        self.cost_state = self.start.get(member)
        self.lamp = True

        return True

    def evaluate(self, algorithm):
        """ Returns an integer representing the score of the state.

        The score is computed as follows: Let n be the state, then the score is computed by the equation
        f(n) = h(n) + g(n),
        where h is the heuristic used and g is the cost from the root down to node n.

        Returns:
            The state's score as an integer.
        """
        if algorithm == "alphastar":
            self.score = self.heuristic() + self.path_cost()
        elif algorithm == "bestfs":
            self.path_cost()
            self.score = self.heuristic()
        return self.score

    def heuristic(self):
        """ Returns the estimated cost of the cheapest path from this state to a goal state.

        The score produced by the heuristic is calculated by taking the maximum speed of
        all the people who are at the starting side of the bridge and still haven't crossed it.

        Returns:
            The heuristic's score as an integer.
        """
        if not self.start:
            return 0
        return max(self.start.values())

    def path_cost(self):
        """ Calculates the path cost from the root-state down to this state.

        The cost from the root-state down to this state, is calculated by taking the path cost of the parent-state
        and adding the cost of this state. The cost of the state is calculated according to the possible move.

        Returns:
           An integer representing the path cost from the root-state down to this stae.
        """
        self.path = self.father.path + self.cost_state
        return self.path

    def get_children(self, algorithm):
        """ Calculates the children of this state.

        The calculation of the children is based on whether the lamp has return to the starting side of the bridge or not.
        If the lamp hasn't returned, then the set of children consists of each person that is on the finishing side. Else,
        the set of children consists of all the combinations of two people that are on the starting side of the bridge.

        Returns:
            A list with the children of this state.
        """
        children = []
        child = State(self.start, self.finish)
        if self.lamp:
            comb = combinations(self.start, 2)
            for i in comb:
                if child.cross_bridge(i):
                    child.set_father(self)
                    child.evaluate(algorithm)
                    children.append(child)
                    child = State(self.start, self.finish)
        else:
            for i in self.finish:
                if child.return_lamp(i):
                    child.set_father(self)
                    child.evaluate(algorithm)
                    children.append(child)
                    child = State(self.start, self.finish)
        return children

    def is_terminal(self, limit):
        """ Checks if this state is a terminal state.

        A state is considered to be terminal if its score has exceeded the time limitation
        or there aren't any more people in the starting side of the bridge.

        Args:
            limit:
                An int representing the time limitation of the Bridge Crossing game.

        Returns:
            True if this is a terminal state, else False.
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

    def get_path(self):
        return self.path

    @staticmethod
    def compare(state):
        """ Utility function used to compare State objects.

        The comparison of State objects is based on the score attribute.

        Args:
            state:
                A State object.

        Returns:
            The value of the score attribute of a State object as an int.
        """
        return state.get_score()

    def print(self):
        print('-----------------------')
        print('Starting side:')
        for person in self.start:
            print(person)
        print('\nFinishing side:')
        for person in self.finish:
            print(person)
        print('-----------------------')
