def input_int():
    a=list(map(int,input().split()))
    return a

def calculate_money(one,two,three):
    money=0
    if (one == two and two == three):
        money += (10000 +one*1000)
    elif (one != two and two != three and one != three):
        big_num = one
        if(two>one or three>one):
            if(two>three):
                big_num = two
            else:
                big_num = three
        money += (1000 +big_num*100)

    else:
        big_num = one
        if(two>one or three>one):
            if(two>three):
                big_num = two
            else:
                big_num = three
        money += (big_num*100)

    return money

def most_money(arr):
    most=0
    for x in arr:
        if(x>most):
            most=x

    print(most)

#참여하는 사람 수 입력
n = int(input())
money_arr=[]
for i in range(n):
    one,two,three=map(int,input().split())
    money_arr.append(calculate_money(one,two,three))
most_money(money_arr)
