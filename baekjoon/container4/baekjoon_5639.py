import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

def post_order(start, end):
    root = pre_order[start]
    idx = start+1

    if start >= end:
        print(root)
        return

    if pre_order[start] < pre_order[start+1] or pre_order[start] > pre_order[end]:
        post_order(start+1, end)
    else:
        while idx <= end:
            if pre_order[idx] > root:
                break
            idx += 1
        post_order(start+1, idx-1)
        post_order(idx, end)
    print(root)

post_order(0, len(pre_order)-1)