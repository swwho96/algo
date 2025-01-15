n = int(input())

def put_queen(row:int):
    global left_right, yx, y_x, cnt, n
    if row == n:
        cnt += 1
        return
    for i in range(n):
        if left_right[i] is False and yx[row+i] is False and y_x[(n-1) + row-i] is False:
            left_right[i] = True
            yx[row+i] = True
            y_x[(n-1)+row-i] = True
            put_queen(row+1) 
            left_right[i] = False
            yx[row+i] = False
            y_x[(n-1)+row-i] = False


left_right = [False] * n
yx = [False] * (2*(n-1)+1)
y_x = [False] * (2*(n-1)+1)
cnt = 0
put_queen(0)
print(cnt)