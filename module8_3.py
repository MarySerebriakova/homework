class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers

        # Проверка VIN и номера автомобиля при создании объекта
        if not self.__is_valid_vin(self.__vin):
            raise IncorrectVinNumber("Некорректный vin номер")
        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers("Некорректный номер автомобиля")

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


# Пример выполняемого кода
try:
    first = Car('Model1', 1000000, 'f123dj')
    print(f'{first.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)

try:
    second = Car('Model2', 300, 'т001тр')
    print(f'{second.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)

try:
    third = Car('Model3', 2020202, 'нет номера')
    print(f'{third.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)