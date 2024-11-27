# 가장 먼 집부터 해결한다

def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries and pickups:
        answer += len(pickups) * 2
        cur_truck = 0
        rest = cap
        while rest > 0:
            if rest >= deliveries[-1]:
                rest -= deliveries[-1]
                deliveries[-1] = 0
            else:
                deliveries[-1] -= rest
                rest = 0
            if cur_truck + pickups[-1] <= cap:
                cur_truck += pickups[-1]
                pickups[-1] = 0
            else:
                pickups[-1] -= (cap-cur_truck)
                cur_truck = cap
            if deliveries[-1] == pickups[-1] == 0:
                deliveries.pop()
                pickups.pop()
            else:
                break
    return answer

print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))