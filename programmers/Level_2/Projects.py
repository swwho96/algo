def solution(plans):
    """
    과제는 시간순으로 진행, 새로운 과제가 주어지면 진행중이던 과제는 잠시 멈춘다
    잠시 멈춘 과제는 최근에 멈춘 순서대로 진행한다
    새로 시작해야 하는 과제를 잠시 멈춘 과제보다 우선한다
    """
    completed = []
    stopped = []
    plans = sorted(plans, key=lambda x: x[1])
    now_name, now_start, now_playtime = plans[0][0], int(plans[0][1].split(":")[0]) * 60 + int(plans[0][1].split(":")[1]), int(plans[0][2])
    for idx in range(1, len(plans)):
        new_name, new_start, new_playtime = plans[idx]
        new_start = int(new_start.split(":")[0]) * 60 + int(new_start.split(":")[1])
        new_playtime = int(new_playtime)

        # 이전 과제가 끝나고, 곧바로 새로운 과제가 시작하는 경우
        if new_start == now_start+now_playtime:
            completed.append(now_name)
            now_name, now_start, now_playtime = new_name, new_start, new_playtime

        elif new_start > now_start + now_playtime: # 새로운 과제 시작까지 시간이 남는 경우
            completed.append(now_name)
            left_time = new_start - (now_start+now_playtime)
            while stopped and left_time>0:
                stop_name, stop_lefttime = stopped.pop()
                if stop_lefttime - left_time > 0:
                    stop_lefttime -= left_time
                    left_time = 0
                    stopped.append([stop_name, stop_lefttime])
                else:
                    left_time -= stop_lefttime
                    completed.append(stop_name)
            now_name, now_start, now_playtime = new_name, new_start, new_playtime

        else: # 진행중인 과제를 멈춰야 하는 경우
            now_playtime -= new_start - now_start
            stopped.append([now_name, now_playtime])
            now_name, now_start, now_playtime = new_name, new_start, new_playtime
    
    # 진행중이던 과제 완료
    completed.append(now_name)

    # 남은 중단된 과제 모두 완료
    while stopped:
        completed.append(stopped.pop()[0])
    return completed