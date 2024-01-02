'''
주어진 수들 중에서 두개를 골라 더한 값이 수들 안에 있으면 좋은수
정렬 후, 앞에서부터 투 포인터로 더해가면서 check에 있는지 확인
'''
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
check = set(A)

result = 0
for i in range(N):
    target = A[i]
    left, right = 0, N-1
    while left < right:
        tmp = A[left] + A[right]
        if tmp > target:
            right -= 1
        elif tmp < target:
            left += 1
        elif tmp == target:
            if left != i and right != i:
                result += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
print(result)