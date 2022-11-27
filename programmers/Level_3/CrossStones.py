def check(stones, mid, k):
    cnt = 0
    for s in stones:
        if s < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True

def solution(stones, k):
    left, right = 0, max(stones)
    while left < right:
        mid = (left+right) // 2
        if check(stones, mid, k):
            left = mid
        else:
            right = mid
    return left