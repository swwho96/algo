# 백준 1978 - 소수찾기
N = int(input())
nums = list(map(int, input().split()))
decimal_cnt = 0
for num in nums:
    if (num == 2) or (num == 3):
        decimal_cnt += 1
        continue
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
        elif i == int(num**0.5):
            decimal_cnt += 1

print(decimal_cnt)
