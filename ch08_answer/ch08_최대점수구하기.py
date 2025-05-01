def DFS(L,time,total):
    global res
    if(time>m):
        return
    if(L==n):
        if(res<total):
            res = total
    else :
        DFS(L+1,time+pt[L],total+ps[L])
        DFS(L+1,time,total)


n, m =map(int,input().split())
ps = []
pt = []
res = 0
for i in range(n):
    a, b = map(int,input().split())
    ps.append(a)
    pt.append(b)
DFS(0,0,0)   
print(res)