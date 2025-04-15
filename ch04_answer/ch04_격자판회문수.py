a = [list(map(int,input().split())) for _ in range (7)]

num = 0
row = 0
col = 0
for i in range(7):
    for j in range(3):
        if(a[i][j]==a[i][j+4]):
            if(a[i][j+1]==a[i][j+3]):
                num += 1

        if(a[j][i]==a[j+4][i]):
            if(a[j+1][i]==a[j+3][i]):
                num += 1


print(num)
            

        