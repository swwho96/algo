from itertools import combinations
def solution(line):
    n = len(line)
    # 교점 구하기
    points = set()
    INF = int(1e15)
    x_list = []
    y_list = []
    left, right, up, down = INF, INF, INF, INF
    two_lines = combinations(range(n), 2)
    for idx1, idx2 in two_lines:
        A, B, E = line[idx1]
        C, D, F = line[idx2]
        if (A*D-B*C) != 0:
            x = (B*F-E*D) / (A*D-B*C)
            y = (E*C-A*F) / (A*D-B*C)
            if x == int(x) and y == int(y): # 두 좌표가 모두 정수일 경우
                x, y = int(x), int(y)
                points.add((x, y))
                x_list.append(x)
                y_list.append(y)
    # 교점 표시
    left, right, up, down = min(x_list), max(x_list), min(y_list), max(y_list)
    col = right - left + 1
    row = down - up + 1
    grid = [['.'] * col for _ in range(row)]
    for point in points:
        x, y = point
        x = x + abs(left) if left < 0 else x - left
        y = y + abs(up) if up < 0 else y - up
        grid[y][x] = '*'
    return [''.join(g) for g in grid[::-1]]