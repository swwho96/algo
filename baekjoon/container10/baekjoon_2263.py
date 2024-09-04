import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_child(in_left, in_right, post_left, post_right):
    if in_left > in_right:
        return
    root = post_order[post_right]
    print(root, end=" ")
    root_index = in_order_index[root]
    offset = root_index - in_left

    find_child(in_left, root_index-1, post_left, post_left+offset-1)
    find_child(root_index+1, in_right, post_left+offset, post_right-1)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_index = {value: index for index, value in enumerate(in_order)}
find_child(0, N-1, 0, N-1)