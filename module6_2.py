class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Допустимые цвета

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner                                  # Владелец
        self.__model = model                                 # Модель (нельзя менять)
        self.__engine_power = engine_power                   # Мощность двигателя (нельзя менять)
        self.__color = color.lower()                         # Цвет автомобиля (нельзя менять)

    def get_model(self):
        return f"Модель: {self.__model}"                    # Возвращает строку с моделью

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"  # Возвращает мощность

    def get_color(self):
        return f"Цвет: {self.__color}"                       # Возвращает цвет

    def print_info(self):
        # Печатает информацию о модели, мощности, цвете и владельце
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        new_color = new_color.lower()                        # Приводим к нижнему регистру для сравнения
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color                         # Меняем цвет, если он допустимый
        else:
            print(f"Нельзя сменить цвет на {new_color}")    # Выводим сообщение если цвет недопустимый


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Ограничение на количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)  # Вызываем инициализацию родительского класса


# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')  # Должен принять

vehicle1.owner = 'Vasyok'  # Изменяем владельца

# Проверяем что поменялось
vehicle1.print_info()