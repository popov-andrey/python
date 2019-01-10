class Shape:
    def __init__(self, width, length):
        self.width = width    # ширина
        self.length = length  # длина

    def print_size(self):
        print('{} на {}'.format(self.width, self.length))


class Square(Shape):
    def area(self):
        return self.width * self.length


a_square = Square(20, 20)
print(a_square.area())
