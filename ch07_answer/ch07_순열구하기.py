def DFS(L):
    global cnt 
    if(L==m):
        for i in range(L):
            print(res[i], end=' ')
        print()
        cnt += 1
    else :
        for i in range(1,n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0


n,m = map(int,input().split())
res = [0]*m
ch = [0]*(n+1)
cnt = 0
DFS(0)
print(cnt)
