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
            if i in res[:L]:  # 이미 사용된 숫자면 제외
                continue
            res[L] = i
            DFS(L+1)



n,m = map(int,input().split())
res = [0]*m
cnt = 0
DFS(0)
print(cnt)