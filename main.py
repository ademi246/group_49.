class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculte_area(self):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width

    def calculate_area(self):
        return self.__length * self.__width
    def info(self):
        area = self.calculate_area()

        print(f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},area:{area}{Figure.unit}")


figure_List = [Square(10),Square(3),Rectangle(1,4),Rectangle(2,8),Rectangle(100,10)]

for figure in figure_List:
    (figure.info())

