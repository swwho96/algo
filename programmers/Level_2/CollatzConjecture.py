def collats_predict(k:int):
    nums = [k]
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k*3 + 1
        nums.append(k)
    return nums

def solution(k, ranges):
    answer = []
    # 우박수열 구하기
    ys = collats_predict(k)
    n = len(ys) - 1 
    xs = [i for i in range(n)]
    # 각 구간 넓이 구하기
    areas = []
    for i in range(n):
        areas.append((ys[i] + ys[i+1]) / 2)
    # 주어진 구간 넓이 구하기
    for s_x, e_x in ranges:
        e_x = n + e_x
        if s_x == e_x:
            answer.append(0.0)
        elif s_x > e_x:
            answer.append(-1.0)
        else:
            answer.append(sum(areas[s_x:e_x]))
    return answer