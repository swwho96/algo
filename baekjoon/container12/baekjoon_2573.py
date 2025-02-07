import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total_ice = sum(cell > 0 for row in board for cell in row)

# 상하좌우 네 방향 (반복문 내에서 매번 튜플 생성하지 않도록 미리 정의)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def ice_check():
    """
    현재 board에서 연결된 빙산 덩어리의 수를 반환하는 함수.
    """
    if total_ice == 0:
        return 0

    # 방문 여부를 관리하는 2차원 리스트 (set보다 빠름)
    visited = [[False] * M for _ in range(N)]
    component_count = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                component_count += 1
                if component_count >= 2:
                    # 두 덩어리가 있으면 더 이상 탐색할 필요 없이 바로 반환
                    return component_count

                # BFS로 연결된 모든 빙산 칸 방문 처리
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            if board[ni][nj] > 0 and not visited[ni][nj]:
                                visited[ni][nj] = True
                                queue.append((ni, nj))
    return component_count

def ice_melting():
    """
    각 빙산 칸 주변의 물의 개수만큼 빙산이 녹는 것을
    동시에 반영하여 board를 갱신하는 함수.
    """
    global total_ice
    # 녹아야 할 칸과 그때 녹는 양을 저장할 리스트
    melting = []
    
    # 전체 board를 순회하며 녹는 양 계산
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                water_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if board[ni][nj] == 0:
                            water_count += 1
                if water_count:
                    melting.append((i, j, water_count))
    
    # 동시에 녹이기 위해 미리 계산한 녹는 양을 반영
    for i, j, water in melting:
        new_height = board[i][j] - water
        if new_height <= 0:
            if board[i][j] > 0:
                total_ice -= 1  # 빙산이 0으로 변한 경우 빙산 개수 감소
            board[i][j] = 0
        else:
            board[i][j] = new_height

year = 0
while total_ice:
    year += 1
    ice_melting()
    if ice_check() >= 2:
        print(year)
        break
else:
    print(0)