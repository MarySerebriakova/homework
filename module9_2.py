first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь, где ключ - строка, значение - длина строки, только для строк с четной длиной
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Примеры вывода
print(first_result)   # Вывод: [10, 8, 8]
print(second_result)  # Вывод: [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)   # Вывод: {'Monitors': 8, 'Computer': 8}