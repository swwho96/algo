def solution(sticker):
    if len(sticker) < 2: return max(sticker)
    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)
    # 첫 스티커를 떼어 냈을 때
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    # 첫 스티커를 떼지 않았을 때
    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    return max(dp1[-2],dp2[-1])