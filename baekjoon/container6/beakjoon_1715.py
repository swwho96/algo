import sys
import heapq
input = sys.stdin.readline
cards = []
n = int(input())
for _ in range(n):
    heapq.heappush(cards, int(input()))
result = 0
while len(cards) > 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    result += a+b
    heapq.heappush(cards, a+b)
print(result)