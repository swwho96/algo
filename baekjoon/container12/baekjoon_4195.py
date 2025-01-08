import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(a, b, parent, size):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

T = int(input().rstrip())
answer = []
for _ in range(T):
    F = int(input().rstrip())
    people_dict = {}
    parent = []
    size = []

    for _ in range(F):
        f1, f2 = input().split()
        
        if f1 not in people_dict:
            people_dict[f1] = len(parent)
            parent.append(len(parent))
            size.append(1)
        if f2 not in people_dict:
            people_dict[f2] = len(parent)
            parent.append(len(parent))
            size.append(1)
        
        union(people_dict[f1], people_dict[f2], parent, size)
        
        root = find_parent(people_dict[f1], parent)
        answer.append(size[root])

for a in answer:
    print(a)
