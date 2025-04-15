n = int(input())
mountain = [[0] * (n+2) for _ in range(n+2)]
how_many=0
for i in range(n): 
    row = list(map(int, input().split())) 
    for j in range(n):  
        mountain[i + 1][j + 1] = row[j] 

for i in range(1,n+1):
    for j in range(1,n+1):
        what = mountain[i][j]
        count = 0
        if(what==0):
            continue

        if(mountain[i][j-1]<what):
            mountain[i][j-1]=0
            count += 1 
        if(mountain[i][j+1]<what):
            mountain[i][j+1]=0
            count += 1 
        if(mountain[i+1][j]<what):
            mountain[i+1][j]=0
            count += 1 
        if(mountain[i-1][j]<what):
            mountain[i-1][j]=0
            count += 1 
        
        if (count==4) :
            how_many+=1

print(mountain)
print(how_many)