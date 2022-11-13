def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems)-1]
    gem = {gems[0]: 1}
    s, e = 0, 0
    while s < len(gems) and e < len(gems):
        if len(gem) == n:
            if e-s < answer[1] - answer[0]:
                answer = [s, e]
            if gem[gems[s]] > 1:
                gem[gems[s]] -= 1
            else:
                del gem[gems[s]]
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            if gems[e] in gem.keys():
                gem[gems[e]] += 1
            else:
                gem[gems[e]] = 1
    return [answer[0]+1, answer[1]+1]