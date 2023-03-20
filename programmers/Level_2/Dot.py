def solution(k, d):
    answer = 0
    x = 0
    while (x**2) ** 0.5 <= d:
        answer += len(range(0, int((d**2-x**2)**0.5)+1, k))
        x += k
    return answer