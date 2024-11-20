
class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors # количество этажей

    def __len__(self):
        return self.number_of_floors     # возвращаем количество этажей

    def __str__(self):
        return f" Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # информация о доме

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors   # сравнение этажей с другим домом
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors   # меньше

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors   # меньше или равно
        return NotImplemented

    def __qt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors  # больше
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors     # больше или равно
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors    # не равно
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value  # Увеличиваем этажи
        return self  # Возвращаем сам объект

    def __radd__(self, value):
        return self.__add__(value)  # Обратное сложение

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House ("ЖК Эльбрус", 10)
h2 = House ("ЖК Акация", 20)

print(h1)  # ЖК Эльбрус,10
print(h2)  # ЖК Акация, 20

print(h1 == h2)  # False

h1 = h1 + 10  # Увеличение на 10 этажей
print(h1)  # ЖК Эльбрус, 20
print(h1 == h2)  # True

h1 += 10  # Увеличение на 10 этажей
print(h1)  # ЖК Эльбрус, 30

h2 = 10 + h2  # Увеличение на 10 этажей через radd
print(h2)  # ЖК Акация, 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2) # False




