from collections import deque

n, m = map(int,input().split())
dq = list(range(1,n+1))
dq = deque(dq)
x = 0
i = 1
while len(dq) != 1 :
    if(i%3==0):
        dq.popleft()
        i += 1
    x = dq.popleft()
    dq.append(x)
    i += 1

print(dq.pop())