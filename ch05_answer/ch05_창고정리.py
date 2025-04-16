L = int(input())

boxes=list(map(int,input().split()))

M = int(input())
high = 0
low = 0
for _ in range(M):
    boxes.sort()
    boxes[0] += 1
    boxes[L-1] -= 1

boxes.sort()
print(boxes[L-1]-boxes[0])