class Square():
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("side_a and side_b should greate than 0")
        self.side_a = side_a

    def get_perimeter(self):
        return self.side_a * 4

    def get_area(self):
        return self.side_a * self.side_a

    def add_area(self, other_figure):
        if not isinstance(other_figure, Square):
            raise ValueError("Нужен класс Rectangle или дочерний")
        return self.get_area() + other_figure.get_area()


