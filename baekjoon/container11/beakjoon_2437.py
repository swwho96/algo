import sys
input = sys.stdin.readline

n = int(input().rstrip())
stones = sorted(list(map(int, input().split())))
cur_sum = 0
for s in stones:
    if cur_sum+1 < s:
        break
    cur_sum += s
print(cur_sum+1)