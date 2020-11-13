class State:
    """
    Represents an instance of the Bridge Crossing problem
    """

    def __init__(self, family: dict, finish = {}):
        self.start = family.copy()
        self.finish = finish.copy()
        self.score = -1
        self.father = None
        self.path = 0


    @classmethod
    def copy_state(cls, start: dict, finish: dict):
        cls.start = start.copy()
        cls.finish = finish.copy()
        cls.score = -1
        cls.father = None
        cls.path = 0

    def get_start(self) -> dict:
        return self.start

    def get_finish(self) -> dict:
        return self.finish

    def get_score(self) -> int:
        return self.score

    def set_start(self, start: dict):
        self.start = start.copy()

    def set_finish(self, finish: dict):
        self.finish = finish.copy()

    def set_score(self, score: int):
        self.score = score

    def cross_the_bridge(self, member1: str, member2: str) -> bool:
        if not self.start:
            return False
        self.finish[member1] = self.start.get(member1)
        self.finish[member2] = self.start.get(member2)
        del self.start[member1]
        del self.start[member2]
        return True


    def return_lamp(self, member: str) -> bool:
        if not self.finish:
            return False
        self.start[member] = self.finish.get(member)
        del self.finish[member]
        return True



    def evaluate(self):
        self.score = self.heuristic() + self.path_cost()

    def heuristic(self) -> int:
        if not self.start:
            return 0
        return max(self.start.values())

    #TODO
    def path_cost(self) -> int:
        #return self.father.path +
        pass

    def get_children(self):
        pass

    def get_father(self) :
        return self.father

    def set_father(self,father):
        self.father = father

    #TODO:heuristic?
    def is_terminal(self,limit: int) -> bool:
        if (self.score >= limit) or (not self.start):
            return True
        return False


    #TODO:repair print
    def print(self):
        for i in self.start:
            print(i)
        print("-----------------------")
        for i in self.finish:
            print(i)
        print("-----------------------")
