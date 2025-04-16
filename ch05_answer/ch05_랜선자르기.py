n, k = map(int,input().split())
a = []
largest=0
for i in range(n):
    num = int(input())
    a.append(num)
    largest=max(largest, num)

count=0
lt = 1
rt = largest
while lt<=rt:
    count = 0
    mid = (lt+rt)//2
    for i in range(n):
        count += a[i]//mid 
        
    if(count>=k):
        answer = mid
        lt = mid+1
    else :
        rt = mid-1
    
print(answer)