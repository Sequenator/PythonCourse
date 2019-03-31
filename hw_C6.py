with open('C:/Users/seque/Downloads/rosalind_subs.txt', 'r') as file:
    a = file.read()

a = a.split()

s = a[0]
t = a[1]

lt = len(t)

for i, b in enumerate(s):
    if b == t[0]:
        if t == s[i:i + lt]:
            print(i + 1)

        
