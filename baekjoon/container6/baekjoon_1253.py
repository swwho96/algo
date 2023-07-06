n = int(input())
A = sorted(list(map(int, input().split())))
result = 0
for idx, m in enumerate(A):
    key = m
    left, right = 0, n-1 
    while left < right:
        if key == A[left] + A[right]:
            if left == idx:
                left += 1
            elif right == idx:
                right -= 1
            else:
                result += 1
                break
        elif key > A[left] + A[right]:
            left += 1
        else:
            right -= 1
print(result)