def solution(m,n,startX,startY,balls):
    def dist_calc(x1,y1,x2,y2):
        return (x1-x2)**2 + (y1-y2)**2
    answer = []
    for x,y in balls:
        tmp_dist = []
        # 왼쪽 벽
        if not (startX >= x and startY == y):
            tmp_dist.append(dist_calc(startX,startY,-x,y))
        # 오른쪽 벽
        if not (startX <= x and startY == y):
            tmp_dist.append(dist_calc(startX,startY,2*m-x,y))
        # 위쪽 벽
        if not (startY <= y and startX == x):
            tmp_dist.append(dist_calc(startX,startY,x,2*n-y))
        # 아래쪽 벽
        if not (startY >= y and startX == x):
            tmp_dist.append(dist_calc(startX,startY,x,-y))

        answer.append(min(tmp_dist))
    return answer