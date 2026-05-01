
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return 'Ошибка: деление на ноль'

print('Калькулятор загружен!')
print(f'2 + 3 = {add(2, 3)}')
print(f'5 - 2 = {subtract(5, 2)}')
