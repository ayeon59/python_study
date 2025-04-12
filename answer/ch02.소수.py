def count_prime(n):
    count=0
    for i in range(2,n+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else :
            count+=1
    print(count)




n = int(input())
count_prime(n)
