def row_sum (arr,k,n):
    sum = 0
    for i in range (n):
        sum += arr[k][i]
    return sum

def col_sum (arr,k,n):
    sum = 0
    for i in range (n):
        sum += arr[i][k]
    return sum

def cross_sum_left (arr,n):
    sum = 0
    for i in range (n):
        sum += arr[i][i]
        
    return sum

def cross_sum_right (arr,n):
    sum = 0
    for i in range (n):
        sum += arr[i][n-i-1]
    return sum

n = int(input())
max_row = 0
max_col = 0
max_cross = 0
rows = n
cols = n
grid = [[0] * cols for _ in range(rows)]
for i in range(n):
    grid[i] = list(map(int,input().split()))

for i in range(n):
    sum_row = row_sum(grid,i,n)
    if(max_row<sum_row):
        max_row = sum_row

for j in range(n):
    sum_col = col_sum(grid,j,n)
    if(max_col<sum_col):
        max_col = sum_col


sum_cross_left = cross_sum_left(grid,n)
if(max_cross<sum_cross_left):
    max_cross = sum_cross_left
sum_cross_right = cross_sum_right(grid,n)
if(max_cross<sum_cross_right):
    max_cross = sum_cross_right    

        
print(max(max_row, max_col, max_cross))