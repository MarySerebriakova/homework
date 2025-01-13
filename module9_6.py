def all_variants(text):
    n = len(text)
    # Внешний цикл для начального индекса
    for start in range(n):
        # Внутренний цикл для конечного индекса
        for end in range(start + 1, n + 1):
            yield text[start:end]  # Возвращаем подпоследовательность

# Пример работы функции
a = all_variants("abc")

for i in a:
    print(i)