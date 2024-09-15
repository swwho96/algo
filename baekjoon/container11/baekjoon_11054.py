import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

def lis(array):
    if len(array) == 0:
        return []
    dp = [array[0]]
    for i in range(len(array)):
        if array[i] > dp[-1]:
            dp.append(array[i])
        else:
            idx = bisect_left(dp, array[i])
            if idx < len(dp):
                dp[idx] = array[i]
    return dp

answer = 1
for i in range(len(A)):
    left, right = lis(A[:i+1]), lis(A[i:][::-1])
    left.pop()
    tmp = left+right[::-1]
    answer = max(answer, len(tmp))
print(answer)