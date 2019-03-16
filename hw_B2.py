with open('C:/Users/seque/Downloads/rosalind_revc.txt', 'r') as file:
    a = file.read()

def reverse(x): 
    r = "" 
    for i in a: 
        r = i + r
    return r

a = a.replace('A', 't')
a = a.replace('T', 'a')
a = a.replace('G', 'c')
a = a.replace('C', 'g')
a = a.upper()

a = reverse(a)
print(a)
