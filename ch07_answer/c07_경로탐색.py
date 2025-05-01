import sys

def DFS(L):
    global cnt
    if(L==n):
        cnt+=1
    
    else : 
        for i in range(1,n+1):
            if(g[L][i]==1 and ch[i]==0):
                ch[i] = 1
                DFS(i)
                ch[i] = 0


n,m = map(int,input().split())
ch = [0]*(n+1)
g = [[0]*(n+1) for _ in range(n+1)] 
cnt = 0
for i in range(m):
    a,b = map(int,input().split())
    g[a][b] = 1
ch[1]=1
DFS(1)

print(cnt)

