import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
q = []
x_dict = defaultdict(list)
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, abs(x))
        heapq.heappush(x_dict[abs(x)], x)
    elif x == 0:
        if q:
            tmp = heapq.heappop(q)
            print(heapq.heappop(x_dict[tmp]))
        else:
            print(0)

# ----------------------------------------------------------

import heapq
import sys
input = sys.stdin.readline
N = int(input())
min_heap = []
max_heap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap))
        else:
            if max_heap:
                print(-heapq.heappop(max_heap))
            else:
                print(0)