def DFS(v):
    global cnt
    if(v==m):
        for j in range(m):
            print(a[j],end =' ')
        print()
        cnt += 1
        return
    else:
        for i in range (1,n+1):
            a[v]=i
            DFS(v+1)


n ,m = map(int,input().split())
a = [0]*m
cnt = 0
DFS(0)
print(cnt)
