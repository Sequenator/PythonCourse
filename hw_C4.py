a = input('Введите элементы квадратного уравнения в порядке уменьшения старшинства через пробел: ')

a = a.split()

b = int(a[1])
c = int(a[2])
a = int(a[0])

D = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print('x - любое число')
elif a == 0:
    if b == 0:
        print('Корней нет')
    else:
        x = -c / b
        print(f'x = {x}')
elif D < 0:
    print('Действительных корней нет')
elif D == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    D = D ** (1/2)
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
