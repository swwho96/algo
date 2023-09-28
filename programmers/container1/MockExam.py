def solution(answers):
    correct_cnt = [0,0,0]
    one = [1,2,3,4,5] # 5으로 나눈 나머지
    two = [2,1,2,3,2,4,2,5] # 8으로 나눈 나머지
    three = [3,3,1,1,2,2,4,4,5,5] # 10으으로 나눈 나머지
    result = []
    
    for i, answer in enumerate(answers):
        if answer == one[i%len(one)]:
            correct_cnt[0] += 1
        if answer == two[i%len(two)]:
            correct_cnt[1] += 1
        if answer == three[i%len(three)]:
            correct_cnt[2] += 1
    
    for i, rank in enumerate(correct_cnt):
        if max(correct_cnt) == rank:
            result.append(i+1)
    return result

# ----------------------------------------------------------

def solution(answers):
    answer = [0, 0, 0]
    N = len(answers)
    one = [1,2,3,4,5] * (N // 5) + [1,2,3,4,5][:N % 5]
    two = [2,1,2,3,2,4,2,5] * (N // 8) + [2,1,2,3,2,4,2,5][:N % 8]
    three = [3,3,1,1,2,2,4,4,5,5] * (N // 10) + [3,3,1,1,2,2,4,4,5,5][:N % 10]
    for idx in range(N):
        if one[idx] == answers[idx]: answer[0] += 1
        if two[idx] == answers[idx]: answer[1] += 1
        if three[idx] == answers[idx]: answer[2] += 1
    return [idx for idx, a in enumerate(answer, start=1) if a == max(answer)]