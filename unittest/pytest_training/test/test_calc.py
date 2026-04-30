from src.calculations import Calculations

class TestCalc:
    calc = Calculations()

    def test_area_of_square(self):
        result = self.calc.area_of_square(10)
        assert result == 100, 'Area of square Error'

    def test_area_of_rect(self):
        result = self.calc.area_of_reat(10, 8)
        assert result == 80, 'Area of react Error'
