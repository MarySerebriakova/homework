def add_everything_up(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return "{:.3f}".format(a + b)  # Форматируем до 3 знаков после запятой
    else:
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))      # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456