import sys
input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N):
    h, w = map(int, input().split())
    table.append([h, w])
for i in range(N):
    bigger_than_me = 1
    for x,y in (table[:i] + table[i+1:]):
        if table[i][0] < x and table[i][1] < y:
            bigger_than_me += 1
    print(bigger_than_me, end=' ')