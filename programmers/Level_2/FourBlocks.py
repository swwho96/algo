def solution(m, n, board):
    answer = 0
    block_check_set = set()
    board = [list(i) for i in board]

    def BoardCheck(b:list)->None:
        for i in range(m-1):
            for j in range(n-1):
                if b[i][j] == b[i][j+1] == b[i+1][j] == b[i+1][j+1] != '0':
                    block_check_set.add((i,j))
                    block_check_set.add((i,j+1))
                    block_check_set.add((i+1,j))
                    block_check_set.add((i+1,j+1))

    def BoardReset(b:list)->None:
        flag = True
        # 블럭 제거
        for x,y in block_check_set:
            b[x][y] = '0'
        # 블럭 내리기
        while flag is True:
            flag = False
            for i in range(m-1,0,-1):
                for j in range(n):
                    if b[i][j] == '0' and b[i-1][j] != '0':
                        flag = True
                        b[i][j] = b[i-1][j]
                        b[i-1][j] = '0'

    while True:
        BoardCheck(board)
        if block_check_set:
            answer += len(block_check_set)
            BoardReset(board)
            block_check_set.clear()
        else:
            break

    return answer