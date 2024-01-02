'''
두 재료를 합쳐 M이 되는 경우를 찾는 문제
합이 M이 되는 조합을 찾고, 각 재료의 개수에 따른 경우의 수를 구하여 결과에 더한다
'''

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
materials = list(map(int, input().split()))

cnt = {}
for m in materials:
    cnt[m] = cnt[m] + 1 if m in cnt else 1

result = 0
while cnt:
    a = list(cnt.keys())[0]
    b = M - a
    if a == b:
        if cnt[a] == 1:
            del cnt[a]
        else:
            result += ((cnt[a] * cnt[a]) // 2)
            del cnt[a]
    elif b in cnt:
        result += (cnt[a] * cnt[b])
        del cnt[a]
        del cnt[b]
    else:
        del cnt[a]

print(result)

# -----------------------------------------------------
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
materials = list(map(int, input().split()))
materials.sort()
left, right = 0, N-1

result = 0
while left < right:
    tmp = materials[left] + materials[right]
    if tmp == M:
        result += 1
        left, right = left+1, right-1
    elif tmp > M:
        right -= 1
    else:
        left += 1

print(result)