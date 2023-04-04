def FindNet(n, now, computers, visited):
    visited[now] = True
    for i in range(n):
        if now != i and computers[now][i] == 1:
            if visited[i] is False:
                FindNet(n, i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] is False:
            FindNet(n, i, computers, visited)
            answer += 1
    return answer

# ---------------------------------------------------

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    parent[max(a,b)] = min(a,b)

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and parent[i] != parent[j]:
                union_parent(i, j, parent)
    for i in range(n):
        parent[i] = find_parent(parent[i], parent)
    return len(set(parent))