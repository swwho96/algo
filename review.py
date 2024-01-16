import sys
input = sys.stdin.readline

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

truths = list(map(int, input().split()))[1:]
for t in truths:
    parent[t] = 0

# 진실을 아는 집합
parties = []
for _ in range(M):
    tmp = list(map(int, input().split()))[1:]
    parties.append(tmp)
    for i in range(len(tmp)-1):
        union(tmp[i], tmp[i+1], parent)

# 과장할 수 있는 파티 구하기
cnt = len(parties)
for p in parties:
    for person in p:
        if find(person, parent) == 0:
            cnt -= 1
            break
print(cnt)
