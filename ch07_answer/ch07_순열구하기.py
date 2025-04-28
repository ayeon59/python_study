def DFS(L):
    global cnt
    if(L==m):
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1,n+1):
            if i in res[:L]:  
                continue
            res[L] = i
            DFS(L+1)

ㄴ

n,m = map(int,input().split())
res = [0]ㄴ*m
cnt = 0
DFS(0)
print(cnt)