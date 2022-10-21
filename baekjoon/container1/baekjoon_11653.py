# 백준 11653 - 소인수분해
N = int(input())
div = 2
while N > 1:
    if N % div == 0:
        N /= div
        print(div)
    else:
        div += 1

####################################################
N = int(input())

prime_num = []

# N까지 소수 찾기
for num in range(2, int(N**0.5)+1):
    flag = True # True 면 소수
    for i in range(2, int(num*0.5)+1):
        if num % i == 0:
            flag = False
    if flag:
        prime_num.append(num)

i = 0
while N > 1:
    if N % prime_num[i] == 0:
        N /= prime_num[i]
        print(prime_num[i])
    else:
        i += 1