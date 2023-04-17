import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total_observer = 0
for i in a:
    # 총감독관 혼자 감독이 가능할 경우
    if i <= b:
        total_observer += 1
    else:
        total_observer += 1
        total_observer += (i-b) // c if (i-b) // c == int((i-b-1) / c) + 1 else int((i-b-1) / c) + 1
print(total_observer)

#  -------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total_observer = n
for i in a:
    i -= b
    if i > 0:
        if i % c == 0:
            total_observer += i//c
        else:
            total_observer += (i//c) + 1
print(total_observer)