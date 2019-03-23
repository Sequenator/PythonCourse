a = input('Введите последовательность слов, разделённых пробелами: ')

a = a.split()

i = 0
l = len(a)
w = 0

for n in a:
    if i == l:
        break
    if w == 0:
        w = len(n)
    elif len(n) < w:
        w = len(n)
    i += 1

print(f'Длина самого короткого слова: {w}')
