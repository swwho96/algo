from collections import deque

def solution(begin, target, words):
    visited = [True for _ in range(len(words))]
    q = deque([[begin, 0]])
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(words):
            distmatch_cnt = 0
            if visited[i] is True:
                for j in range(word):
                    if word[i] != words[i][j]:
                        dismatch_cnt += 1
                if distmatch_cnt == 1:
                    q.append([word[i], cnt+1])
                    visited[i] = False
    return 0