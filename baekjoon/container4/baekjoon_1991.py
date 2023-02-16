class Node():
    def __init__(self, head, left, right) -> None:
        self.head = head
        self.left = left
        self.right = right

def preorder(node):
    print(node.head, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.head, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.head, end='')


import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for _ in range(n):
    h, l, r = input().split()
    tree[h] = Node(h, l, r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])