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

if __name__ == '__main__':
    while True:
        try:
            a = float(input('Введите первое число (или 0 для выхода): '))
            if a == 0:
                print('Выход из калькулятора.')
                break
            b = float(input('Введите второе число: '))
            operation = input('Введите операцию (+, -, *, /): ')

            if operation == '+':
                print(f'{a} + {b} = {add(a, b)}')
            elif operation == '-':
                print(f'{a} - {b} = {subtract(a, b)}')
            elif operation == '*':
                print(f'{a} * {b} = {multiply(a, b)}')
            elif operation == '/':
                print(f'{a} / {b} = {divide(a, b)}')
            else:
                print('Неизвестная операция. Используйте +, -, * или /.')
        except ValueError:
            print('Ошибка: введите корректное число.')
        except Exception as e:
            print(f'Произошла непредвиденная ошибка: {e}')
