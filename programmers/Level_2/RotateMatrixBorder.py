def solution(rows, columns, queries):
    answer = []
    matrix = []
    # 행렬 생성
    for i in range(1, rows*columns, columns):
        tmp = []
        for j in range(i, i+columns):
            tmp.append(j)
        matrix.append(tmp)
    # 테두리 회전
    for q in queries:
        minimum = rows*columns+1
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        tmp = matrix[x1][y1]
        for a in range(x1, x2): # 왼쪽
            if minimum > matrix[a+1][y1]:
                minimum = matrix[a+1][y1]
            matrix[a][y1] = matrix[a+1][y1]
            
        for a in range(y1, y2): # 아래
            if minimum > matrix[x2][a+1]:
                minimum = matrix[x2][a+1]
            matrix[x2][a] = matrix[x2][a+1]
            
        for a in range(x2, x1, -1): # 오른쪽
            if minimum > matrix[a-1][y2]:
                minimum = matrix[a-1][y2]
            matrix[a][y2] = matrix[a-1][y2]
            
        for a in range(y2, y1, -1): # 위
            if minimum > matrix[x1][a-1]:
                minimum = matrix[x1][a-1]
            matrix[x1][a] = matrix[x1][a-1]
        if minimum > tmp:
            minimum = tmp
        matrix[x1][y1+1] = tmp
        answer.append(minimum)
    return answer