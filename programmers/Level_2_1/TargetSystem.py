def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])
    e = 0
    for i in range(len(targets)):
        if targets[i][0] >= e:
            answer += 1
            e = targets[i][1]
    return answer