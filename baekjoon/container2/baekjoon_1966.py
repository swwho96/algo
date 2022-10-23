import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, idx = map(int, sys.stdin.readline().split())
    importances = deque(map(int, sys.stdin.readline().split()))
    printed = deque([False for _ in range(N)]) # 출력 여부 저장
    cnt = 0 # 출력 순서
    while True:
        if importances[0] == max(importances) and printed[0] is False:
            cnt += 1
            importances[0] = -1
            printed[0] = True
        if idx == 0 and printed[idx] is True:
            break
        idx = (idx - 1) if idx > 0 else (N-1)
        importances.rotate(-1)
        printed.rotate(-1)
    print(cnt)