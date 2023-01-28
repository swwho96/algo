import sys
input = sys.stdin.readline
import heapq
from queue import PriorityQueue
T = int(input())
for _ in range(T):
    n = int(input())
    q = PriorityQueue()
    for _ in range(n):
        c, num = input().split()
        if c == 'I':
            heapq.heappush(q, int(num))
        elif c == 'D':
            if not q:
                continue
            else:
                if num == '1':
                    q.pop(q.index(max(q)))
                elif num == '-1':
                    heapq.heappop(q)
    # 비어있다면 'EMPTY', 아니라면 [최대, 최소]
    if q:
        print(max(q), min(q))
    else:
        print('EMPTY')