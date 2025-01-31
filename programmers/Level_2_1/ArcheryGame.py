def solution(n, info):
    
    # 해당 점수를 획득 한다 or 못한다
    def get_score(arrow:int, targets:list, now_target:int):
        if now_target == 10 or arrow == 0:
            nonlocal score_diff, answer
            if arrow > 0:
                targets[-1] += arrow
            a, l = 0, 0
            for i in range(11):
                if (info[i] > 0) and (info[i] >= targets[i]):
                    a += 10-i
                elif (targets[i] > 0) and (targets[i] - info[i] > 0):
                    l += 10-i
            if l - a > 0:
                if (l - a > score_diff) or (l - a == score_diff and targets[::-1] > answer[::-1]):
                    score_diff = l-a
                    answer[:] = targets
            targets[-1] -= arrow
            return
        
        # 이긴다 = 해당 점수에 화살을 쏜다
        if arrow >= info[now_target]+1:
            targets[now_target] += info[now_target]+1
            arrow -= info[now_target]+1
            get_score(arrow, targets, now_target+1)
            arrow += info[now_target]+1
            targets[now_target] -= info[now_target]+1
        
        # 진다 = 해당 점수에 쏘지 않고 다음 점수로 넘어간다
        get_score(arrow, targets, now_target+1)
        
    answer = [-1]
    score_diff = 0
    get_score(n, [0 for _ in range(11)], 0)
    
    return answer