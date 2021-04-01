class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.value = [self.x, self.y]

    def to_string(self):
        return self.value
