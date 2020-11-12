class State:
    """
    Represents an instance of the Bridge Crossing problem
    """

    def __init__(self, family: dict):
        self.start = family.copy()
        self.finish = {}
        self.score = -1

    @classmethod
    def copy_state(cls, start: dict, finish: dict):
        cls.start = start.copy()
        cls.finish = finish.copy()
        cls.score = -1

    def get_start(self) -> dict:
        return self.start

    def get_finish(self) -> dict:
        return self.finish

    def get_score(self) -> int:
        return self.score

    def set_start(self, start: dict):
        self.start = start.copy

    def set_finish(self, finish: dict):
        self.finish = finish.copy

    def set_score(self, score: int):
        self.score = score

    def cross_the_bridge(self, member1: str, member2: str):
        self.finish[member1] = self.start.get(member1)
        self.finish[member2] = self.start.get(member2)
        del self.start[member1]
        del self.start[member2]
        #TODO: calculate cost

    def return_lamp(self, member: str):
        self.start[member] = self.finish.get(member)
        del self.finish[member]
        #TODO: calculate cost


    def evaluate(self):
        pass

    def heuristic(self):
        pass

    def function_g(self):
        pass

    def print(self):
        for i in self.start:
            print(i)
        print("-----------------------")
        for i in self.finish:
            print(i)
        print("-----------------------")
