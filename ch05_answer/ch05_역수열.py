n = int(input())

arrays=list(map(int,input().split()))
answers=[0]*n
cnt = 0
for i in range(n):
    cnt = arrays[i]
    answers[cnt] = i
print(answers)