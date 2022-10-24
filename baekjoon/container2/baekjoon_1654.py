import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
len_lines = []
for _ in range(N):
    len_lines.append(int(sys.stdin.readline().rstrip()))
left = max(len_lines)
right = 0
while left - right > 1:
    can_make_len = 0
    pivot = int((left+right) / 2)
    for l in len_lines:
        can_make_len += int(l / pivot)
    if can_make_len >= K:
        right = pivot
    else:
        left = pivot
can_make_len = 0
for l in len_lines:
    can_make_len += int(l/left)
print(left if can_make_len >= K else right)