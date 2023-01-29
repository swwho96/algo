import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict
T = int(input())
for _ in range(T):
    n = int(input())
    max_q, min_q = [], []
    number_cnt_dict = defaultdict(int)
    for _ in range(n):
        c, num = input().split()
        if c == 'I':
            number_cnt_dict[int(num)] += 1
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
        elif c == 'D':
            if num == '1':
                while max_q:
                    tmp = -heapq.heappop(max_q)
                    if number_cnt_dict[tmp] > 0:
                        number_cnt_dict[tmp] -= 1
                        break
            elif num == '-1':
                while min_q:
                    tmp = heapq.heappop(min_q)
                    if number_cnt_dict[tmp] > 0:
                        number_cnt_dict[tmp] -= 1
                        break
    result = sorted(number_cnt_dict.items(), key=lambda x: x[0], reverse=True)
    answer = []
    for i, v in result:
        if v > 0:
            answer.append(i)
    if answer:
        print(answer[0], answer[-1])
    else:
        print('EMPTY')