M = int(input())
N = int(input())
flag = False
sum_num = 0
min_num = N
if N <= 1:
    print(-1)
else:
    for num in range(N, M - 1, -1):
        if 1 < num <= 3:
            flag = True
            sum_num += num
            min_num = num
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
                elif i == int(num**0.5):
                    flag = True
                    sum_num += num
                    min_num = num

    if flag is True:
        print(sum_num)
        print(min_num)
    else:
        print(-1)
