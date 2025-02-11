import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().rstrip())
left, right = [], []
for _ in range(N):
    A, B = map(int, input().split())
    left.append([A,B])
    right.append([B,A])

left.sort()
right.sort()

def cross_check(line_list:list):
    prev = [line_list[0][1]]
    for a, b in line_list:
        if prev[-1] < b:
            prev.append(b)
        else:
            prev[bisect_left(prev, b)] = b
    return len(line_list) - len(prev)

print(min(cross_check(left), cross_check(right)))