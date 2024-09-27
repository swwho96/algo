import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
tree = {i: {'child':[], 'parent':None} for i in range(1,N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def makeTree(cur:int, parent:int):
    global tree
    for node in graph[cur]:
        if node != parent:
            tree[cur]['child'].append(node)
            tree[node]['parent'] = cur
            makeTree(node, cur)

makeTree(1, -1)
for i in range(2, N+1):
    print(tree[i]['parent'])