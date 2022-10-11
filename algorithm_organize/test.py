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

'''-------------------------------------------------'''

# 단어 분리 하기
from queue import deque
word = 'centerminus'
word_dict = ['cent', 'center', 'term', 'terminus', 'min', 'us', 'rm', 'minus']
q = [word[0]]
result = []
new = []
def dfs(new, word):
    while q:
        char = q.pop()
        for w in word_dict:
            if len(word) < 2:
                result.append(new)
                print(new)
                new = []
                break
            if word.startswith(w):
                new.append(w)
                tmp = w[-1] + word.replace(w, '')
                q.append(tmp[0])
                dfs(new, tmp)
            new.pop()

dfs(new, word)
print(result)