n = int(input())

arrays=list(map(int,input().split()))
answers=[0]*n
cnt = 0
for i in range(n):
    cnt = arrays[i]
    find = 0
    for j in range(n):
        if(find==cnt):
            answers[j] = i+1
        if(answers[j]==0):
            find += 1
print(answers)