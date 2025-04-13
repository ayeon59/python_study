n = int(input())
answer=list(map(int,input().split()))
sum_score = 0
add_score = 0
for i in range(n):
    if answer[i] == 1:
        add_score += 1
        sum_score += add_score
    else:
        add_score = 0

print(sum_score)





