import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

cnt = 0
def solve(arr):
    global cnt
    if len(arr) == 1:
        return arr
    N = len(arr) // 2
    left, right = solve(arr[:N]), solve(arr[N:])
    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            cnt += len(left) - i
    if i < len(left):
        for p in range(i, len(left)):
            sorted_arr.append(left[p])
    elif j < len(right):
        for q in range(j, len(right)):
            sorted_arr.append(right[q])
    return sorted_arr

A = solve(A)
print(cnt)