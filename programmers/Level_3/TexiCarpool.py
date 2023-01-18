def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    # 2차원 그래프 생성
    graph = [[INF] * (n+1) for i in range(n+1)]
    # 그래프 초기화
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    # 요금표 입력
    for data in fares:
        c, d, cost = data[0], data[1], data[2]
        graph[c][d] = cost
        graph[d][c] = cost

    # 플로이드워셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    # 최소 비용 계산
    for k in range(1, n+1):
        fare = graph[s][k] + graph[k][a] + graph[k][b]
        if fare < answer:
            answer = fare
    return answer