from collections import deque

n, m=map(int,input().split())
weight=list(map(int,input().split()))

weight.sort()
weight=deque(weight)

cnt=0

while weight:
    if(len(weight)==1):
        cnt += 1
        break
    if(weight[0]+weight[-1]>m):
        cnt += 1
        weight.pop()
    else :
        cnt += 1
        weight.pop()
        weight.popleft()
    

print(cnt)
