def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()  # Вызов внутренней функции

# Вызов test_function для выполнения inner_function
test_function()

# вызов inner_function вне функции
inner_function()  #oшибка NameError