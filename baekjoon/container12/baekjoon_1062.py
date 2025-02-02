import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(set(word[4:-4]))
if K < 5:
    print(0)
else:
    base = {'a','n','t','i','c'}
    needed = set()
    for w in words:
        for char in w:
            if char not in base:
                needed.add(char)
    if len(needed) + 5 <= K:
        print(N)
    else:
        combis = combinations(needed, K-5)
        answer = 0
        for combi in combis:
            learned = set(combi) | base
            tmp_cnt = 0
            for w in words:
                for char in w:
                    if char not in learned:
                        break
                else:
                    tmp_cnt += 1
            answer = max(answer, tmp_cnt)
        print(answer)