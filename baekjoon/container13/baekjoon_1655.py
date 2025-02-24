import sys
import heapq
input = sys.stdin.readline

max_heap = []
min_heap = []
N = int(input().rstrip())
for _ in range(N):
    num = int(input().rstrip())
    heapq.heappush(max_heap, -num)

    if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(max_heap) > len(min_heap)+1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    if len(max_heap) == len(min_heap):
        print(min(-max_heap[0], min_heap[0]))
    else:
        print(-max_heap[0])