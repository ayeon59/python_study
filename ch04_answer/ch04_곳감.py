n = int(input())
persimmon = [[0]* n for _ in range(n)]

for i in range (n): 
    persimmon[i] = list(map(int,input().split()))

m = int(input())
for i in range(m):
    where,toward,how = map(int,input().split())
    if(toward==0):
        for j in range(how):
            object = persimmon[where-1].pop(0)
            persimmon[where-1].append(object)
    else:
        for j in range(how):
            object = persimmon[where-1].pop()
            persimmon[where-1].insert(0,object)

sum = 0
s = -1
e = n+1
for i in range(n):
    if(i<=n//2):
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1

    for j in range(s,e):
        sum += persimmon[i][j]

print(sum)