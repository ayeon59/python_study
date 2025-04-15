n, k = map(int,input().split())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

count=0
lt = 1
rt = 1000
while lt<=rt:
    count = 0
    mid = (lt+rt)//2
    for i in range(n):
        count += a[i]//mid 
        
    if(count<k):
        rt = mid-1
    else :
        answer = mid
        lt = mid+1
    
    
print(answer)