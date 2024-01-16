import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
A, B, C = map(int, input().split())
first = [A,B,C]
graph = [[1,2], [0,2], [0,1]]
answer = set()

# 물을 다 부어 없애거나, 물병이 꽉 차거나
# 현재 위치에서 물을 부을 위치를 선택

def dfs(now, bottles):
    global answer, first
    if tuple(bottles) in answer:
        return
    answer.add(tuple(bottles))
    for now, i in [(1,0),(1,2),(0,1),(0,2),(2,1),(2,0)]:
        p = bottles.copy()
        if p[i]+p[now] <= first[i]:
            p[i] += p[now]
            p[now] = 0
        else:
            p[now] -= (first[i] - p[i])
            p[i] = first[i]
        dfs(i, p)


dfs(2, [0,0,C])
result = set()
for a in answer:
    if a[0] == 0:
        result.add(a[2])
print(' '.join(map(str, sorted(list(result)))))