# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# nodes = list(map(int, input().split()))
# del_node = int(input().rstrip())

# visited = [False] * N
# graph = [[] for _ in range(N)]
# for u, v in enumerate(nodes):
#     if v == -1:
#         root = u
#     if v != -1:
#         graph[u].append(v)
#         graph[v].append(u)

# if del_node == root:
#     print(0)
# else:
#     visited[root] = True
#     q = [root]
#     answer = 0
#     while q:
#         cur = q.pop()
#         leaf = True
#         for node in graph[cur]:
#             if node != del_node:
#                 if visited[node] == False:
#                     visited[node] = True
#                     leaf = False
#                     q.append(node)
#         if leaf is True:
#             answer += 1

#     print(answer)


def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
print(arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)