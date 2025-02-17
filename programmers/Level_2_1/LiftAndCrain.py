from collections import deque
def solution(storage, requests):
    
    def fork_lift(target:str):
        nonlocal left_container
        tmp_container = []
        visited = [[False] * (M+2) for _ in range(N+2)]
        visited[0][0] = True
        q = deque([(0,0)])
        while q:
            r, c = q.popleft()
            for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<=N+1 and 0<=nc<=M+1 and visited[nr][nc] is False:
                    if storage[nr][nc] == target:
                        left_container -= 1
                        visited[nr][nc] = True
                        tmp_container.append((nr,nc))
                    elif storage[nr][nc] == '#':
                        q.append((nr,nc))
                        visited[nr][nc] = True
        for i,j in tmp_container:
            storage[i][j] = '#'
        return

    def crain(target:str):
        nonlocal left_container
        cnt = 0
        tmp_container = []
        for i in range(1,N+1):
            for j in range(1,M+1):
                if storage[i][j] == target:
                    tmp_container.append((i,j))
                    left_container -= 1
        for i, j in tmp_container:
            storage[i][j] = '#'
        return
    
    N, M = len(storage), len(storage[0])
    left_container = N*M
    storage = [['#']*(M+2)] + [['#']+list(s)+['#'] for s in storage] + [['#']*(M+2)]
    
    for request in requests:
        if len(request) == 1:
            fork_lift(request[0])
        elif len(request) == 2:
            crain(request[0])
            
    return left_container