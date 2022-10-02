def solution(triangle):
    if len(triangle) == 1:
        return (triangle[0])
    while len(triangle) > 1:
        sum_result = []
        max_result = []
        # 상단 두줄 꺼내기
        up, down = triangle.pop(0), triangle.pop(0)
        # 더하기
        for i in range(len(up)):
            sum_result += [up[i]+down[i], up[i]+down[i+1]]
        # 두 개씩 max()하기
        for i in range(1, len(sum_result)-1, 2):
            max_result.append(max(sum_result[i], sum_result[i+1]))
        # 삼각형에 합치기
        max_result = [sum_result[0]] + max_result + [sum_result[-1]]
        triangle = [max_result] + triangle
    print(triangle)
    return max(*triangle)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))