from itertools import permutations
def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    total_permut = list(permutations(range(N), N))
    for order in total_permut:
        game_cnt = 0
        this_game_k = k
        for game in order:
            if dungeons[game][0] > this_game_k:
                continue
            else:
                game_cnt += 1
                this_game_k -= dungeons[game][1]

        if game_cnt > answer:
            answer = game_cnt
    return answer