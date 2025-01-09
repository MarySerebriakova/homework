import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем содержимое файла
                    text = file.read().lower()
                    # Убираем пунктуацию
                    text = re.sub(r"[',.=!?;:-]", '', text)
                    # Разбиваем текст на слова
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            try:
                index = words.index(word) + 1  # Позиция начинается с 1
                results[file_name] = index
            except ValueError:
                results[file_name] = None  # Слово не найдено

        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            results[file_name] = count

        return results


# Пример использования
finder2 = WordsFinder('test_file.txt')

# Печатаем все слова из файлов
print(finder2.get_all_words())

# Печатаем позицию слова 'TEXT' (в 3-ем месте)
print(finder2.find('TEXT'))

# Печатаем количество слов 'teXT' (4 раза)
print(finder2.count('teXT'))