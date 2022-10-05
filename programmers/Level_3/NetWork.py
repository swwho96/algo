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