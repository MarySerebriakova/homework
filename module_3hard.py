def calculate_structure_sum(data_structure):
    total_sum = 0

    if isinstance(data_structure, int):  # Если элемент - целое число
        return data_structure  # Возвращаем число

    elif isinstance(data_structure, str):  # Если элемент - строка
        return len(data_structure)  # Возвращаем длину строки

    elif isinstance(data_structure, (list, tuple, set)):  # Если элемент - список,кортеж или множество
        for item in data_structure:  # Обрабатываем каждый элемент
            total_sum += calculate_structure_sum(item)
                                                # Рекурсивно добавляем к общей сумме

    elif isinstance(data_structure, dict):  # Если элемент - словарь
        for key, value in data_structure.items():
            total_sum += len(key)  # Добавляем длину ключа
            total_sum += calculate_structure_sum(value)
                                             # Рекурсивно обрабатываем значение

    return total_sum  # Возвращаем общую сумму


data_structure = [
    [1, 2, 3],                                  # Сумма: 1 + 2 + 3 = 6
    {'a': 4, 'b': 5},                           # Сумма: len('a') + 4 + len('b') + 5 = 1 + 4 + 1 + 5 = 11
    (6, {'cube': 7, 'drum': 8}),                # Сумма: 6 + len('cube') + 7 + len('drum') + 8 = 6 + 4 + 7 + 4 + 8 = 29
    "Hello",                                    # Сумма: len('Hello') = 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])      # Сумма: 2 + len('Urban') + len('Urban2') + 35 = 2 + 5 + 6 + 35 = 48
]

result = calculate_structure_sum(data_structure)
print(result)  # 99