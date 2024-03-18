from abc import ABC, abstractmethod
from Square import Square
from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle

class Figure(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

square = Square(10) 
print(square.get_area())
triangle1 = Triangle(13, 14, 15)
print(triangle1.get_area())
print(triangle1.get_perimeter())
