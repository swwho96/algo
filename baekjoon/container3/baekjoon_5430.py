import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    nums = input().rstrip()
    if nums == '[]': 
        nums = []
    else: 
        nums = deque(list(map(int, nums.replace('[', '').replace(']','').split(','))))
    d = ['left', 'right']
    cnt = 0
    front = d[cnt%2]
    for op in p:
        if op == 'R':
            cnt += 1
            front = d[cnt%2]
        elif op == 'D':
            if not nums:
                print('error')
                break
            else:
                if front == 'left':
                    nums.popleft()
                elif front == 'right':
                    nums.pop()
    else:
        if front == 'right':
            nums.reverse()
        print(str(list(nums)).replace(' ', ''))