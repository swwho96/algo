import heapq
def solution(operations):
    num_list = []
    heapq.heapify(num_list)
    for op_num in operations:
        op, num = op_num.split()[0], int(op_num.split()[1])
        if op == 'D' and len(num_list) == 0:
            continue
        if op == 'I':
            heapq.heappush(num_list, num)
        elif op == 'D' and num == 1:
            num_list.pop()
        elif op == 'D' and num == -1:
            num_list.pop(0)
    return [max(num_list), min(num_list)] if len(num_list)>0 else [0,0]