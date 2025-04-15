n = int(input())
arr_n = list(map(int,input().split()))
m = int(input())
arr_m = list(map(int,input().split()))

arr_sum=[]
for i in range(n+m):
    if(i<n):
        arr_sum.append(arr_n[i])
    else :
        arr_sum.append(arr_m[i-n])

arr_sum.sort()

print(' '.join(map(str, arr_sum)))