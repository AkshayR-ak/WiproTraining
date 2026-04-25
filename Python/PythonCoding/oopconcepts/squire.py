from oopconcepts.formulamethods import FormulaMethods


class Squire(FormulaMethods):
    def __init__(self, s):
        self.side = s

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side