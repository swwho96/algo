'''
ENTER 이후 첫 채팅은 반드시 이모티콘이다.
채팅에서 사용된 이모티콘의 수를 반환한다.
'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())
gomgom = 0
hi_set = set()
for i in range(N):
    log = input().rstrip()
    if log == 'ENTER':
        gomgom += len(hi_set)
        hi_set = set()
    else:
        hi_set.add(log)
gomgom += len(hi_set)
print(gomgom)