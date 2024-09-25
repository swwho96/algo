import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = defaultdict(list)
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

nodes = {}
for i in range(1, N+1):
    nodes[i] = {'child': [], 'parent': None}

def maketree(cur:int, parent:int):
    global graph
    for node in graph[cur]:
        if node != parent:
            nodes[cur]['child'].append(node)
            nodes[node]['parent'] = cur
            maketree(node, cur)

size = {node: 0 for node in nodes}
def countsubtreenode(cur):
    size[cur] = 1
    for child in nodes[cur]['child']:
        countsubtreenode(child)
        size[cur] += size[child]


maketree(R, -1)
countsubtreenode(R)

for _ in range(Q):
    U = int(input().rstrip())
    print(size[U])