import sys

def DFS(L):
    global total
    if(L==N):
        total = 0
        for i in range(N):
            total += answer[i]*b[i]
        if(total==F):
            print(answer)
            sys.exit()
            
    else:
        for i in range(1,N+1):
            if(ch[i]==0):
                answer[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0 



N,F = map(int,input().split())
answer = [0]*N
total = 0
b = [1]*N
ch = [0]*(N+1)
for i in range(1,N):
    b[i] = b[i-1]*(N-i)//i
DFS(0)