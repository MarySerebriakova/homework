first = int(input ("Введите первое число"))
second = int(input ("Введите второе число"))
third = int(input ("Введите третье число"))
if first == second == third:
    print (3)                 #все числа равны
elif first == second or first == third or second == third:
    print(2)                             #2 из 3 чисел равны
else:
    print(0)                        #равных чисел нет