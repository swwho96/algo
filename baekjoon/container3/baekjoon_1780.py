import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def count_papers(grid, x, y, size):
    ones = 0
    zeros = 0
    neg_ones = 0
    sub_size = size // 3

    if all(grid[i][j] == 1 for i in range(x, x + size) for j in range(y, y + size)):
        ones += 1
    elif all(grid[i][j] == 0 for i in range(x, x + size) for j in range(y, y + size)):
        zeros += 1
    elif all(grid[i][j] == -1 for i in range(x, x + size) for j in range(y, y + size)):
        neg_ones += 1
    else:
        for i in range(3):
            for j in range(3):
                sub_x = x + i * sub_size
                sub_y = y + j * sub_size
                sub_result = count_papers(grid, sub_x, sub_y, sub_size)
                ones += sub_result[0]
                zeros += sub_result[1]
                neg_ones += sub_result[2]

    return (ones, zeros, neg_ones)

def truncate_matrix(grid):
    return count_papers(grid, 0, 0, len(grid))

one, zero, neg_ones = truncate_matrix(board)
print(neg_ones)
print(zero)
print(one)