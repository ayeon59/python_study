def sum_apple(arr,line,center,gap):
    apple = arr[line][center]
    for i in range(1,gap+1):
        apple += arr[line][center+i]
        apple += arr[line][center-i]
    return apple

n = int(input())
tree = [[0]* n for _ in range(n)]
apple = 0
for i in range(n):
    tree[i] = list(map(int, input().split()))

center = n//2
for j in range(n):
    gap = j if j <= center else n - j - 1
    apple += sum_apple(tree,j,center,gap)

print(apple)