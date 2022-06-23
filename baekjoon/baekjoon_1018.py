row, col = map(int, input().split())
chess_board = []
start_with_bw = ['BW'*4, 'WB'*4]
start_with_wb = ['WB'*4, 'BW'*4]


# 체스판 입력받기
for _ in range(row):
    chess_board.append(input())

# 원본 체스판 생성하기
origin_chess_board_bw = [start_with_bw[i % 2] for i in range(row)]
origin_chess_board_wb = [start_with_wb[i % 2] for i in range(row)]

answer = []

# 체스판 검사하기 (wbwb~ 이거나 bwbw~ 이거나)
for i in range(row-7):
    for j in range(col-7):
        bw_cnt = 0
        wb_cnt = 0
        # 8*8 크기 보드판 검사하기
        for a in range(i, i+8):
            for b in range(j, j+8):
                if chess_board[a][b] != origin_chess_board_bw[a-i][b-j]:
                    bw_cnt += 1
                if chess_board[a][b] != origin_chess_board_wb[a-i][b-j]:
                    wb_cnt += 1
        answer.append(min(bw_cnt, wb_cnt))


print(min(answer))
