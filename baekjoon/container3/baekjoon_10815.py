import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
n = int(input())
sangun = list(map(int, input().split()))
sangun.sort()
m = int(input())
cards = list(map(int, input().split()))
for num in cards:
    if bisect_right(sangun, num) - bisect_left(sangun, num) == 0:
        print(0, end=' ')
    else:
        print(1, end=' ')

# ------------------------------------------------------------------

import sys
sangun, cards = sys.stdin.read().splitlines()[1::2]
sangun = set(sangun.split())
cards = cards.split()
for num in cards:
    if num in sangun:
        print(0, end=' ')
    else:
        print(1, end=' ')