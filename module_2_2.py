first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third:
    print('Среди данных чисел 3 одинаковых')
elif first == second != third or first != second == third or second != first == third:
    print('Среди данных чисел 2 одинаковых')
else:
    print('Среди данных чисел 0 одинаковых')