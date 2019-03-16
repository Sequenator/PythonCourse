with open('C:/Users/seque/Downloads/rosalind_hamm.txt', 'r') as file:
    a = file.readlines()

b = a[1]
a = a[0]

j = 0
n = 0

for i in a:
    if i != b[j]:
        n = n + 1
    j = j + 1

print(n)
        
