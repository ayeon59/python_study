def DFS(L,start):
    global cnt
    if(L==m):
        for i in range(L):
            print(res[i], end=' ')
        print()
        cnt += 1
    else :   
        for i in range(start,n+1):
            res[L]=i
            DFS(L+1,i+1)


n,m = map(int,input().split())
res = [0]*m
ch = [0]*(n+1)
cnt = 0
DFS(0,1)
print(cnt)
