def sn(n):
    l=[]
    for i in range(2, n+1):
        for k in l:
            if i % k == 0:
                break
        else:
            l.append(i)
            yield i
for num in sn(int(input())):
    print(num, end = ' ')
