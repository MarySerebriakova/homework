numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(number)
    elif number >= 2:
        not_primes.append(number)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)
