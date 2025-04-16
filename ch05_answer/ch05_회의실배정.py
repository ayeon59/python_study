n = int(input())
meeting=[]
for i in range(n):
    s,e = map(int,input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1],x[0]))

endpoint=0
cnt = 0
for s, e in meeting:
    if s>=endpoint:
        cnt += 1
        endpoint = e
print(cnt)