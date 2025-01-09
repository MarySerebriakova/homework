# Сначала создадим файл test_file.txt с вашим текстом.
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде,\n")
    f.write("Используйте его для самопроверки.\n")
    f.write("Успехов в решении задачи!\n")
    f.write("text text text\n")

import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем имена файлов в формате списка
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    words_list = []  # Список для хранения слов из текущего файла
                    for line in lines:
                        line = line.lower()  # Приводим к нижнему регистру
                        # Убираем пунктуацию
                        line = line.translate(str.maketrans('', '', string.punctuation + " -"))
                        words = line.split()  # Разбиваем строку на слова
                        words_list.extend(words)  # Добавляем слова в общий список
                    all_words[file_name] = words_list  # Записываем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()  # Игнорируем регистр
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Возвращаем позицию (индекс + 1)

        return result

    def count(self, word):
        result = {}
        word = word.lower()  # Игнорируем регистр
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count_result = words.count(word)  # Считаем количество слов
            if count_result > 0:
                result[file_name] = count_result  # Добавляем в результат только если найдено хотя бы одно

        return result

# Пример использования
finder = WordsFinder('test_file.txt')

# Все слова
print(finder.get_all_words())

# Позиция слова 'TEXT'
print(finder.find('TEXT'))

# Количество слов 'teXT' в тексте
print(finder.count('teXT'))