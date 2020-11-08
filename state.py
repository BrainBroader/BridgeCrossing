class State:

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
        self.start = start

    def set_finish(self, finish: dict):
        self.finish = finish

    def set_score(self, score: int):
        self.score = score








