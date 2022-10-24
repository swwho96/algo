import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
len_lines = []
for _ in range(N):
    len_lines.append(int(sys.stdin.readline().rstrip()))
left = max(len_lines)
right = 1
while left >= right:
    can_make_len = 0
    pivot = int((left+right) / 2)
    for l in len_lines:
        can_make_len += int(l / pivot)
    if can_make_len >= K:
        right = pivot + 1
    else:
        left = pivot - 1
print(left)