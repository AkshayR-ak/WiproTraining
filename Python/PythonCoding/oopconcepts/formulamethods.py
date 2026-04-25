from abc import ABC, abstractmethod


class FormulaMethods(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass