# # 음료수 얼려 먹기 - bfs
# from queue import deque
# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(input()))

# icecream = 0

# def bfs(graph, x, y):
#     q = deque([(x,y)])
#     while q:
#         x, y = q.popleft()
#         for a, b in zip([-1,1,0,0], [0,0,-1,1]):
#             nx = x + a
#             ny = y + b
#             if 0 <= nx < N and 0 <= ny < M:
#                 if graph[nx][ny] == '0':
#                     q.append((nx, ny))
#                     graph[nx][ny] = '#'

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == '0':
#             bfs(graph, i, j)
#             icecream += 1

# print(icecream)

#'''-------------------------------------------------'''

# 단어 분리 하기
# from queue import deque
# word = 'centerminus'
# word_dict = ['cent', 'center', 'term', 'terminus', 'min', 'us', 'rm', 'minus']
# q = [word[0]]
# result = []
# new = []
# def dfs(new, word):
#     while q:
#         char = q.pop()
#         for w in word_dict:
#             if len(word) < 2:
#                 result.append(new)
#                 print(new)
#                 new = []
#                 break
#             if word.startswith(w):
#                 new.append(w)
#                 tmp = w[-1] + word.replace(w, '')
#                 q.append(tmp[0])
#                 dfs(new, tmp)
#             new.pop()

# dfs(new, word)
# print(result)

direction_x = [-1,0,1,0]
direction_y = [0,1,0,-1]

def TurnLeft(di):
    return di - 1 if di >= 1 else 3

def Move(x, y, di):
    return x+direction_x[di], y+direction_y[di]

def Back(x, y, di):
    return x-direction_x[di], y-direction_y[di]

N, M = map(int, input().split())
x, y, di = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
cnt = 1

while True:
    print(maps)
    flag = False
    for _ in range(4):
        di = TurnLeft(di)
        nx, ny = Move(x, y, di)
        if 0<=nx<N and 0<=ny<M and maps[nx][ny] == 0:
            flag = True
            cnt += 1
            maps[x][y] = 9
            maps[nx][ny] = 9
            x, y = nx, ny
            break
    if flag is True:
        continue
    else:
        nx, ny = Back(x, y, di)
        if maps[nx][ny] == 1:
            print('The End')
            break
        else:
            x, y = nx, ny

print(cnt)