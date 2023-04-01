from collections import deque
def solution(priorities, location):
    order_list = deque(priorities)
    cur = location
    print_cnt = 0
    while cur >= 0:
        if order_list[0] >= max(order_list):
            order_list.popleft()
            cur -= 1
            print_cnt += 1
        else:
            order_list.rotate(-1)
            if cur == 0:
                cur = len(order_list) - 1
            else:
                cur -= 1
    
    return print_cnt

# --------------------------------------------------------------------


from collections import deque
def solution(priorities, location):
    cnt = 0
    priorities = deque(priorities)
    while priorities:
        j = priorities.popleft()
        for i in priorities:
            if i > j:
                priorities.append(j)
                location = (location-1) if location > 0 else (len(priorities)-1)
                break
        else:
            cnt += 1
            if location == 0:
                break
            location = (location-1) if location > 0 else (len(priorities)-1)
    return cnt