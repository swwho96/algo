# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

# def find_child(in_left, in_right, post_left, post_right):
#     if in_left > in_right:
#         return
#     root = post_order[post_right]
#     print(root, end=" ")
#     root_index = in_order_index[root]
#     offset = root_index - in_left

#     find_child(in_left, root_index-1, post_left, post_left+offset-1)
#     find_child(root_index+1, in_right, post_left+offset, post_right-1)

# N = int(input())
# in_order = list(map(int, input().split()))
# post_order = list(map(int, input().split()))

# in_order_index = {value: index for index, value in enumerate(in_order)}
# find_child(0, N-1, 0, N-1)

def makeTree(inorder_left:int, inorder_right:int, postorder_left:int, postorder_right:int)->object:
    if inorder_left > inorder_right or postorder_left > postorder_right:
        return None
    
    print("inorder", inorder[inorder_left:inorder_right+1], "postorder", postorder[postorder_left:postorder_right+1])
    # 현재 서브트리의 루트 값
    root_value = postorder[postorder_right]
    print(root_value, end=' ')

    # inorder에서 root_value의 위치 찾기
    pivot = inorder[inorder_left:inorder_right+1].index(root_value) + inorder_left

    # 왼쪽 서브트리 크기
    left_subtree_size = pivot - inorder_left
    
    # 왼쪽 서브트리 재귀 호출
    makeTree(inorder_left, pivot - 1, postorder_left, postorder_left + left_subtree_size - 1)

    # 오른쪽 서브트리 재귀 호출
    makeTree(pivot + 1, inorder_right, postorder_left + left_subtree_size, postorder_right - 1)



N = int(input().rstrip())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
makeTree(0, N-1, 0, N-1)