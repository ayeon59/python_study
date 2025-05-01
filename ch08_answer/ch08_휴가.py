def DFS(L,time,profit):
    global res
    if time >= n:
        res = max(res, profit)
        return
    
    else:
        if(time>pt[L]):
            return
        if time + pt[L] <= n:
            DFS(L + 1, time + pt[L], profit + pp[L]) 
        DFS(L + 1, time, profit)  

n = int(input())
res = 0
pt = []
pp = []
for i in range(n):
    a, b = map(int,input().split())
    pt.append(a)
    pp.append(b)
DFS(0,0,0)

print(res)