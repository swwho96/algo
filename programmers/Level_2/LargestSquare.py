# 시간초과 풀이
def solution(board):
    answer = 0
    for n in range(min(len(board), len(board[0])), 0, -1): # 도장 크기 n x n
        for i in range(len(board)-n+1):
            for j in range(len(board[0])-n+1):
                for row in range(i, i+n):
                    if set(board[row][j:j+n]) != set([1]):
                        break
                else:
                    answer = n * n
                    return answer
    return answer

# __________________________________________________________________________________

def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2