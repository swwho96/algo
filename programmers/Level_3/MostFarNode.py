from collections import deque
def solution(n, edge):
    graph = [[] for i in range(len(edge)+1)]
    distance = [-1] * (n+1)
    # 그래프 연결하기
    for e in edge:
        start, end = e
        graph[start].append(end)
        graph[end].append(start)
    distance[1] = 0
    q = deque([1])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now] + 1
    return distance.count(max(distance))