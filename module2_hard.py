
def generate_password(n):

    if n < 3 or n > 20:
        return "Значение должно быть от 3 до 20"

    password = ""
    used_pairs = set()


    for i in range(1, 21):
        for j in range(i, 20):
            if i != j:
                pair_sum = i + j
                if pair_sum > 0 and n % pair_sum == 0:
                    pair = f"{i}{j}"
                    if pair not in used_pairs:
                        used_pairs.add(pair)
                        password += pair

    return password


n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print(f"Пароль: {result}")