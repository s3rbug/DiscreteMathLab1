import random


class SetLogic:
    def __init__(self):
        self.fields = [set(), set(), set()]  # a, b, c
        self.power = [1, 1, 1]
        self.universal = [1, 10]
        self.x = self.y = self.z = self.z_python = set()

    def set_power(self, which, value):
        self.power[which] = value

    def set_universal(self, which, value):
        self.universal[which] = value

    def get_universal(self, which):
        return self.universal[which]

    def set_field(self, which, value: set):
        self.fields[which] = value

    def calculate(self, which):
        seq = [i for i in range(self.universal[0], self.universal[1] + 1)]
        random.shuffle(seq)
        self.fields[which] = set()
        for i in range(self.power[which]):
            self.fields[which].add(seq[i])
        self.calculate_xyz()

    def generate(self):
        for i in range(len(self.fields)):
            self.calculate(i)
        self.calculate_xyz()

    def calculate_xyz(self):
        uni = set([i for i in range(self.universal[0], self.universal[1] + 1)])
        self.x = uni - self.fields[2]
        self.y = self.fields[0]
        self.z = self.calculate_z()
        self.z_python = self.calculate_z_python()

    def calculate_z_python(self):
        return self.x | self.y

    def calculate_z(self):
        y = list(self.y)
        z = list(self.x)
        for i in y:
            if i not in z:
                z.append(i)
        return set(z)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_z_python(self):
        return self.z_python
