# import sys
# input = sys.stdin.readline

# N = int(input())
# A = set(map(int,input().split()))
# M = int(input())
# numbers = list(map(int, input().split()))
# for n in numbers:
#     if n in A:
#         print(1)
#     else:
#         print(0)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))
for n in numbers:
    left, right = 0, len(A)-1
    flag = False
    while left <= right:
        mid = (left+right) // 2
        if A[mid] == n:
            flag = True
            break
        elif mid > n:
            right = mid-1
        else:
            left = mid+1
    print(1) if flag is True else print(0)