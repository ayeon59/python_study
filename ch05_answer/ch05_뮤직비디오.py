def count(capacity,music):
    songs=0
    cnt = 1
    for x in music:
        if(songs+x>capacity):
            cnt += 1
            songs = x
        else :
            songs += x

    return cnt

n, m = map(int,input().split())
music= list(map(int,input().split()))

start = 1
end = sum(music)
maxx = max(music)
while start<=end:
    mid = (start+end)//2
    if mid>=maxx and count(mid,music)<=m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)