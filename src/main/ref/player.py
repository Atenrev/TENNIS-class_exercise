class Player:
    points = 0

    def __init__(self, name):
        self.name = name

    def add_point(self):
        self.points = self.points + 1

    def get_points(self):
        return self.points

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __nq__(self, other):
        if self.name != other.name:
            return True
        else:
            return False
