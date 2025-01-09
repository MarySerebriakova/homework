def custom_write(file_name, strings):
    # Создаем словарь для хранения позиций и строк
    strings_positions = {}

    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Сохраняем текущее положение (байт) перед записью строки
            byte_position = file.tell()

            # Записываем строку в файл и добавляем перевод строки
            file.write(string + '\n')

            # Добавляем значение в словарь с кортежем (номер строки, байт начала строки)
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)