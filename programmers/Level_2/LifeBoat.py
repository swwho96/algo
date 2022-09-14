# 효율성 - 시간초과
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        flag = False
        left_weight = limit - people[0]
        for i in range(1,len(people)):
            if left_weight >= people[i]:
                people.remove(people[i])
                people.pop(0)
                flag = True
                answer += 1
                break
        if flag is False:
            answer += 1
            people.pop(0)
    return answer

def solution(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer