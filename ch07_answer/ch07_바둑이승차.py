def DFS(L, sum):
    global max_weight
    if L == num:
        if sum > max_weight:
            max_weight = sum
        return
    if sum + a[L] <= max:
        DFS(L + 1, sum + a[L])
    DFS(L + 1, sum)


max, num = map(int,input().split())
max_weight = 0
sum = 0
a = []
for i in range(num):
    x = int(input())
    a.append(x)

DFS(0,0)
print(max_weight)