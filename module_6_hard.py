import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count # список сторон
        self.__color = color if self.__is_valid_color(*color) else [0,0,0] # список цветов в формате RGB
        self.filled = False # закрашенный, bool

    def get_color(self): # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b): # проверка на корректность, все значения (целые числа от 0 до 255)
        return all(isinstance(i,int) and 0 <= i <= 255 for i in (r,g,b))

    def set_color(self, r, g, b): # изменяет атрибут __color на соответствующие значения, проверив на корректность
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def __is_valid_sides(self,*sides): # возвтащает True если стороны целые положительные числа и совпадают с текущими, иначе Fals
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self): # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides): # принимает новые стороны, если количество != sides_count, то не изменять, иначе менять
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self): # возвращает площадь круга
        return math.pi * self.__radius ** 2

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius == self.get_sides()[0] / (2 * math.pi)

class Triangle(Figure):
    sides_count = 3

    def get_square(self): # возвращает площадь треугольника
        sides = self.get_sides()
        p = sum(sides) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides): # переопределяем __sides сделав список из 12 одинак. сторон(передается 1 сторона)
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self): # возвращает объем куба
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())