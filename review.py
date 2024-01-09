import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)
answer = 0
while len(cards) > 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    answer += a + b
    heapq.heappush(cards, a+b)

print(answer)