class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_outside(self, x, y):
        return not (0 <= x < self.width and 0 <= y < self.height)

    def __str__(self):
        return f"{self.width}, {self.height}"
