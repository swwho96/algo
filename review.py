import sys
input = sys.stdin.readline
N = int(input())
left, right = 1, 1
answer = 1
cnt = 0
while left <= right <= N:
    if answer < N:
        right += 1
        answer += right
    elif answer >= N:
        if answer == N:
            cnt += 1
        answer -= left
        left += 1

print(cnt)