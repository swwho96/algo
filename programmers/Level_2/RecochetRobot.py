def solution(board):
    answer = int(10e9)
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    
    def foward(r:int, c:int, d:int, cnt:int):
        global answer
        nr, nc = r+direction[d][0], c+direction[d][1]
        # 갈 수 없다면 종료
        if not (0<=nr<len(board) and 0<=nc<len(board[0])):
            return
        # G에 도착했다면 answer 업데이트 후 종료
        if board[nr][nc] == 'G':
            answer = min(cnt, answer)
            return
        # 다음이 장애물이나 가장자리라면 방황전환 및 cnt+1:
        if not (0<=nr<len(board) and 0<=nc<len(board[0])) or board[nr][nc] == 'D':
            foward(r, c, (d+1)%4, cnt+1)
            foward(r, c, (d+2)%4, cnt+1)
            foward(r, c, (d+3)%4, cnt+1)
        # 다음으로 갈 수 있다면 방향 그대로 다음칸 이동
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == '.':
            foward(nr, nc, d, cnt)
            
    # R위치 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                r, c = i, j
    # 출발
    foward(r, c, 0, 0)
    foward(r, c, 1, 0)
    foward(r, c, 2, 0)
    foward(r, c, 3, 0)
    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))