import sys
input = sys.stdin.readline

'''
큐에서 첫 숫자는 버리고, 그 다음 숫자를 제일 끝에 넣는다
'''
from collections import deque
N = int(input())

cards = deque([i for i in range(1, N+1)])
trash = 0
while True:
    trash = cards.popleft()
    if cards:
        cards.append(cards.popleft())
    else:
        break
print(trash)