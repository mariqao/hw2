
class Triangle():

    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("side_a and side_b should greate than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        self.area = (self.get_perimeter() * (self.get_perimeter() - self.side_a) * (self.get_perimeter() - self.side_b) * (self.get_perimeter() - self.side_c)) ** 0.5
        return self.area

    def add_area(self, other_figure: str):
        if not isinstance(other_figure, Triangle):
            raise ValueError("Нужен класс Rectangle или дочерний.")
        return self.get_area() + Square.get_area()

