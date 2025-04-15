def count_gap(len):
    cnt=1
    ep=dx[0]
    for i in range(1,n):
        if(dx[i]-ep)>=len:
            cnt+=1
            ep = dx[i]
    return cnt


n,c=map(int,input().split())
dx=[]
for i in range(n):
    num = int(input())
    dx.append(num)
dx.sort()

start = 0
end = max(dx)
while(start<=end):
    mid = (start+end)//2
    if count_gap(mid)>=c:
        res = mid
        start = mid + 1
    else :
        end = mid -1

print(res)
