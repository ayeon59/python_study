def DFS(v,s):
    global res
    if(res<v):
        return
    if(s>m):
        return
    if(s==m):
        if(v<res):
            res = v
        return
    else:
        for i in range(n):
            DFS(v+1,s+a[i])

n = int(input())
a = list(map(int,input().split()))
m = int(input())
a.sort(reverse=True)
res = 27400000
cnt = 0
sum = 0
DFS(0,0)
print(res)