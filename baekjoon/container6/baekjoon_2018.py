n = int(input())
left, right = 1, 2
result = left + right
cnt = 1
while right < n:
    if result == n:
        cnt += 1
        right += 1
        result += right
    elif result > n:
        result -= left
        left += 1
    else:
        right += 1
        result += right
print(cnt)