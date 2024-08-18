# import sys
# input = sys.stdin.readline


# S = input().rstrip()
# bomb = input().rstrip()
# result = []
# for s in S:
#     result.append(s)
#     while len(result)>=len(bomb) and ''.join(result[-len(bomb):]) == bomb:
#         for _ in range(len(bomb)):
#             result.pop()
# print(''.join(result) if result else 'FRULA')

import time

# 리스트 생성
test_list = ['a'] * 1000000 + ['bomb']

# pop()을 반복하는 방식
start = time.time()
result = test_list[:]
for _ in range(100000):
    for _ in range(4):
        result.pop()
print("pop() 방식 소요 시간:", time.time() - start)

# del 슬라이싱을 사용하는 방식
start = time.time()
result = test_list[:]
for _ in range(100000):
    del result[-4:]
print("del 슬라이싱 방식 소요 시간:", time.time() - start)