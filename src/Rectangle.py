class Rectangle():

    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("side_a and side_b should greate than 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, other_figure):
        if not isinstance(other_figure, Rectangle):
            raise ValueError("Нужен класс Rrectangle или дочерний")
        return self.get_area() + other_figure.get_area()


