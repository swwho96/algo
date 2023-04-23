def solution(sequence, k):
    answer = [int(1e9),0, 0]
    dp = [0, sequence[0]]
    for i in range(1, len(sequence)):
        dp.append(dp[-1]+sequence[i])
    left, right = 1, 1
    while True:
        if right >= len(dp) or left > right:
            break
        tmp = dp[right]-dp[left]+sequence[left-1]
        if tmp == k:
            if (answer[0] > (right-left)):
                answer = [right-left, left-1, right-1]
            right += 1
        elif tmp < k:
            right += 1
        elif tmp > k:
            left += 1
    return answer[1:]