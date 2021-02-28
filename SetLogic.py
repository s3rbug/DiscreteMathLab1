import random


class SetLogic:
    def __init__(self):
        self.fields = [set(), set(), set()]     # a, b, c
        self.power = [1, 1, 1]
        self.universal = [1, 10]

    def set_power(self, which, value):
        self.power[which] = value

    def set_universal(self, which, value):
        self.universal[which] = value

    def get_universal(self, which):
        return self.universal[which]

    def get_max_power(self):
        return max(self.power)

    def set_field(self, which, value: set):
        self.fields[which] = value

    def calculate(self, which):
        seq = [i for i in range(self.universal[0], self.universal[1])]
        random.shuffle(seq)
        self.fields[which] = set()
        for i in range(self.power[which]):
            self.fields[which].add(seq[i])

    def generate(self):
        for i in range(len(self.fields)):
            self.calculate(i)


