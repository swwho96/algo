def solution(order):
    answer = 0
    order = order[::-1]
    backup = []
    belt = [i for i in range(len(order), 0, -1)]
    while order:
        if belt and belt[-1] == order[-1]:
            belt.pop()
            order.pop()
            answer += 1
        elif backup and backup[-1] == order[-1]:
            backup.pop()
            order.pop()
            answer += 1
        else:
            if belt:
                backup.append(belt.pop())
            else:
                break
    return answer