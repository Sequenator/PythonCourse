a = input('Введите последовательночть чисел, разделённых пробелами: ')

a = a.split()

print('Следующие элементы последовательности больше предыдущего:')

i = 1

l = len(a)

for n in a:
    if i == l:
        break
    if a[i] > n:
        print(a[i])
    i += 1