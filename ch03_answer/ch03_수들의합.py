def count_sum(arr,total,start):
    i = start
    sum = 0
    while i < len(arr):
        if (sum>=total):
            break
        sum += arr[i]
        i += 1
    
    if(sum == total):
        
        return True
    else :
        return False


n,m=map(int,input().split())
a = list(map(int,input().split()))
count = 0
i = 0
for i in range(n):
    if(count_sum(a,m,i)):
        count+= 1

print(count)
