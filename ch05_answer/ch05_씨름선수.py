n = int(input())
sports=[]
for i in range(n):
    x, y = map(int,input().split())
    sports.append((x,y))

sports.sort(reverse=True)
cnt = 0
heavy = 0
for x, y in sports:
    if(y>heavy):
        cnt += 1
        heavy = y
print(cnt)