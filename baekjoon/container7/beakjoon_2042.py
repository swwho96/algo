import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
treeheight = 0
length = n

while length != 0:
    length //= 2
    treeheight += 1

treesize = 2 ** (treeheight+1)
leftnodestartindex = treesize // 2 - 1
tree = [0] * (treesize + 1)

# 트리에 값 저장
for i in range(leftnodestartindex+1, leftnodestartindex + n + 1):
    tree[i] = int(input())

def setTree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

setTree(treesize-1)

def change(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index //= 2

def getsum(s, e):
    partsum = 0
    while s <= e:
        if s % 2 == 1:
            partsum += tree[s]
            s += 1
        if e % 2 == 0:
            partsum += tree[e]
            e -= 1
        s = s//2
        e = e//2
    return partsum

for _ in range(m+k):
    q, s, e = map(int, input().split())
    if q == 1:
        change(leftnodestartindex + s, e)
    elif q == 2:
        s = s + leftnodestartindex
        e = e + leftnodestartindex
        print(getsum(s, e))