import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
coins.sort()
answer = [float('inf') for _ in range(k+1)]
answer[0] = 0
for i in range(1, k+1):
    for coin in coins:
        if i-coin >= 0:
            answer[i] = min(answer[i], answer[i-coin]+1)
print(answer[k] if answer[k]!=float('inf') else -1)

# --------------------------------------------------

import sys
from collections import deque

def coin_change_bfs(N, K, coins):
    # 큐 초기화: (현재 금액, 동전 개수)
    queue = deque([(0, 0)])
    visited = set([0])  # 방문한 금액 저장

    while queue:
        current, count = queue.popleft()

        # 목표 금액 도달 시 최소 동전 개수 반환
        if current == K:
            return count

        for coin in coins:
            next_amount = current + coin
            
            # 범위를 넘지 않고, 방문하지 않은 경우만 큐에 추가
            if next_amount <= K and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, count + 1))

    return -1  # 목표 금액을 만들 수 없는 경우

# 입력 처리
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 결과 출력
print(coin_change_bfs(N, K, coins))