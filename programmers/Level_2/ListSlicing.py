def solution(n, left, right):
    start, end = left//n, right//n
    left, right = left-(start*n), right-(start*n)
    result = []
    for i in range(start, end+1):
        result += [i+1 for _ in range(i+1)] + [j for j in range(i+2, n+1)]
    return result[left:right+1]