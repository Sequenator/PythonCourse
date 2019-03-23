a = input('Введите целое положительное число: ')

a = str(a)

l = len(a)
i = 0
sum = 0
com = 1

for n in a:
    if i == l:
        break
    n = int(n)
    sum = sum + n
    com = com * n
    i += 1

print(f'Сумма цифр числа: {sum}')
print(f'Произведение цифр числа: {com}')
