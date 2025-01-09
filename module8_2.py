def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    # Перебираем все элементы numbers
    for number in numbers:
        try:
            # Пытаемся добавить к результату, если это число
            result += number
        except TypeError:
            # Обрабатываем исключение, если элемент не числового типа
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Пытаемся посчитать сумму с помощью функции personal_sum
        total, incorrect_data = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    try:
        # Пытаемся посчитать среднее арифметическое
        average = total / (len(numbers) - incorrect_data)  # Учитываем некорректные данные
    except ZeroDivisionError:
        return 0

    return average


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанные типы
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректные данные