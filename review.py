import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
tmp = N
treesize = 0
while tmp != 0:
    tmp //= 2
    treesize += 1

treesize = pow(2, treesize+1)
leftstart = treesize // 2 - 1
tree = [0] * (treesize+1)

for idx in range(leftstart+1, leftstart+N+1):
    tree[idx] = int(input().rstrip())

def initTree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

initTree(treesize-1)

def change(index, value):
    diff = value-tree[index]
    while index > 0:
        tree[index] += diff
        index = index // 2

def getsum(s, e):
    answer = 0
    while s <= e:
        if s % 2 == 1:
            answer += tree[s]
            s += 1
        if e % 2 == 0:
            answer += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return answer

for _ in range(M+K):
    q, s, e = map(int, input().split())
    if q == 1:
        change(leftstart+s, e)
    elif q == 2:
        s += leftstart
        e += leftstart
        print(getsum(s,e))