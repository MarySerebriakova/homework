my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0
while counter < len(my_list):
    number = my_list[counter]
    if number == 0:
        counter += 1
        continue
    if number < 0:
        counter += 1
        break
    print(number)
    counter += 1