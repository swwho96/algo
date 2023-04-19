import sys
from collections import deque
input = sys.stdin.readline
gear = [[]]
for _ in range(4):
    gear.append(deque(list(map(int, input().rstrip()))))
k = int(input())
for _ in range(k):
    attached_gear = [[], [-1, gear[1][2]], [gear[2][6], gear[2][2]], [gear[3][6], gear[3][2]], [gear[4][6],-1]]
    turned = [0,0,0,0,0]
    q = deque([list(map(int, input().split()))])
    while q:
        idx, op = q.popleft()
        if turned[idx] == 0:
            gear[idx].rotate(op)
            turned[idx] = 1
        if idx == 1 and attached_gear[idx][1] != attached_gear[idx+1][0]:
            if turned[idx+1] == 0:
                gear[idx+1].rotate(-op)
                turned[idx+1] = 1
                q.append([idx+1, -op])
        if idx==2 or idx==3:
            if attached_gear[idx][0] != attached_gear[idx-1][1] and turned[idx-1] == 0:
                gear[idx-1].rotate(-op)
                turned[idx-1] = 1
                q.append([idx-1, -op])
            if attached_gear[idx][1] != attached_gear[idx+1][0] and turned[idx+1] == 0:
                gear[idx+1].rotate(-op)
                turned[idx+1] = 1
                q.append([idx+1, -op])
        if idx == 4:
            if attached_gear[idx][0] != attached_gear[idx-1][1] and turned[idx-1] == 0:
                gear[idx-1].rotate(-op)
                turned[idx-1] = 1
                q.append([idx-1, -op])

# 점수계산
score = sum([g[0] * (2**i) for i, g in enumerate(gear[1:])])
print(score)