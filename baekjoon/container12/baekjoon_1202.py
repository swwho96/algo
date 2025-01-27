import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N):
    weight, value = map(int, input().split())
    jewels.append((weight, value))

for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

max_heap = []
total_value = 0
j = 0

for bag in bags:
    # 현재 가방에 넣을 수 있는 모든 보석을 힙에 추가
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(max_heap, -jewels[j][1])
        j += 1
    
    # 가장 가치가 큰 보석을 가방에 넣기
    if max_heap:
        total_value += -heapq.heappop(max_heap)

# 결과 출력
print(total_value)