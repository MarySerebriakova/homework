class House:
    def __init__(self, name, number_of_floors):
        self.name = name               # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        # Проверяем, существует ли указанный этаж
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Выводим номера этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)

# Пример использования класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)