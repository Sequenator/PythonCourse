with open('C:/Users/seque/Downloads/rosalind_fib.txt', 'r') as file:
    a = file.read()

a = a.split()

n = a[0]
k = a[1]
a1 = 1
a2 = 1

for i in range(int(n) - 2):
    m = a2
    a2 = a1 * int(k) + a2
    a1 = m
    
print(a2)
