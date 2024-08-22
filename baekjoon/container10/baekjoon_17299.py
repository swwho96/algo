import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

# 숫자별 등장 횟수
cnt_dict = Counter(A)

# 다음 숫자 확인하기
check = []
result = [-1] * N
for i in range(N):
    while check and cnt_dict[A[check[-1]]] < cnt_dict[A[i]]:
        result[check.pop()] = A[i]
    check.append(i)
print(' '.join(map(str,result)))