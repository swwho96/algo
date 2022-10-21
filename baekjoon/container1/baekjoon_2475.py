numbers = list(map(int, input().split()))
answer = 0
for num in numbers:
    answer += (num ** 2)
print(answer % 10)
