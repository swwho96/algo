import sys
input = sys.stdin.readline

N, M = map(int, input().split())
k = 0
length = N
while length != 0:
    length //= 2
    k += 1

treeSize = pow(2, k+1)
tree = [sys.maxsize] * treeSize
startIdx = 2**k
for i in range(N):
    tree[i+startIdx] = int(input())

def setTree(i):
    while i != 1:
        tree[i//2] = min(tree[i//2], tree[i])
        i -= 1

setTree(treeSize-1)

def getMin(s, e):
    minimum = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            minimum = min(minimum, tree[s])
            s += 1
        if e % 2 == 0:
            minimum = min(minimum, tree[e])
            e -= 1
        s = s // 2
        e = e // 2
    return minimum

for _ in range(M):
    s, e = map(int, input().split())
    s += startIdx - 1
    e += startIdx - 1
    print(getMin(s,e))