# Задача 1 - Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Задача 2 - Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")

    return write_everything


# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задача 3 - Метод __call__
import random


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())  # Случайный выбор
print(first_ball())  # Случайный выбор
print(first_ball())  # Случайный выбор