import sys
import heapq
input = sys.stdin.readline
n = int(input())
nums = []
result = 0
positive, negative = [], []
zero, one = 0, 0
for _ in range(n):
    a = int(input())
    if a > 1:
        heapq.heappush(positive, -a)
    elif a == 0:
        zero += 1
    elif a == 1:
        one += 1
    elif a < 0:
        heapq.heappush(negative, a)
while len(positive) > 1:
    x, y = -heapq.heappop(positive), -heapq.heappop(positive)
    result += x*y
if positive:
    result += -heapq.heappop(positive)

while len(negative) > 1:
    x, y = heapq.heappop(negative), heapq.heappop(negative)
    result += x*y

if zero == 0 and negative:
    result += heapq.heappop(negative)

result += one
print(result)