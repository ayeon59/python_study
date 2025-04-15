def check_row(arr):
    for i in range(9):
        for k in range(1,10):
            if (arr[i].count(k)!=1):
                return False
    return True

def check_col(arr):
    for i in range(9):
        for k in range(1,10):
            if ((arr[k].count(i))!=1):
                return False
    return True

def check_box(arr):
    for i in range(0, 9, 3):         # 행 시작점
        for j in range(0, 9, 3):     # 열 시작점
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(arr[i + x][j + y])
            if sorted(box) != list(range(1, 10)):
                return False
    return True


sudoku = list(map(int,input().split()))
while True:
    if(check_row(sudoku)):
        if(check_col(sudoku)):
            if(check_box(sudoku)):
                print("YES")
                break
    print("NO")
    break