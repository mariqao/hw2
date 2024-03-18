class Circle():
    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError("side_a and side_b should greate than 0")
        self.radius = radius

    def get_perimeter(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return self.radius * math.pi ** 2

    def add_area(self, other_figure):
        if not isinstance(other_figure, Circle):
            raise ValueError("Нужен класс Rrectangle или дочерний")
        return self.get_area() + other_figure.get_area()



