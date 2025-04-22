from collections import deque

essential = input()  
n = int(input())
memo=[]
example=[]
for i in range(n):
    dq = deque(essential)
    example = deque(list(input()))
    while example:
        n1 = example.popleft()
        n2 = dq.popleft()
        if(n1==n2):
            memo.append(n1)
        else : 
            dq.append(n2)
    memo = ''.join(memo)
    if(str == memo) :
        print("#%d YES" %(i+1))
    else :
        print("#%d NO" %(i+1))

