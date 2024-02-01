import sys
input = sys.stdin.readline

M = int(input())
colors = list(map(int, input().split()))
K = int(input())
total = sum(colors)
answer = 0
for color in colors:
    tmp = 1
    tmp_total = total
    tmp_color = color
    for _ in range(K):
        tmp *= (tmp_color / tmp_total)
        tmp_color -= 1
        tmp_total -= 1
    answer += tmp
print(answer)