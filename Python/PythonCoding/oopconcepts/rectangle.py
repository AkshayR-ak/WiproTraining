from oopconcepts.formulamethods import FormulaMethods


class Rectangle(FormulaMethods):
    def __init__(self, s, l):
        self.side = s
        self.length = l

    def calculate_area(self):
        return self.side * self.length

    def calculate_perimeter(self):
        return 2 * (self.side + self.length)