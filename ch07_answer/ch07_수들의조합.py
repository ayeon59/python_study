def DFS(L,s):
    global cnt
    if(L==k):
        if(sum(res)%m==0):
            cnt += 1
    else:
        for i in range(s,n):
            res[L] = num[i]
            DFS(L+1,i+1)

n,k = map(int,input().split())
num = list(map(int,input().split()))
res = [0]*k
m = int(input())
cnt = 0

num.sort()

DFS(0,0)

print(cnt)

