import sys
input = sys.stdin.readline

N = int(input().rstrip())
buildings = list(map(int, input().split()))
laser = [0] * N
stack = [(0,0)] # (위치, 높이)
for idx, height in enumerate(buildings):
    while stack and stack[-1][1] < height:
        stack.pop()
    if stack:
        laser[idx] = stack[-1][0]+1
    stack.append((idx, height))
print(' '.join(map(str,laser)))