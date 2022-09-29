def QuadStamp(arr:list, N:int)->list:
    result = [0,0]
    for x in range(0, len(arr), N):
        for y in range(0, len(arr[0]), N):
            zero_stamp = True
            one_stamp = True
            for i in range(x, x+N):
                for j in range(y, y+N):
                    if arr[i][j] != 0: zero_stamp = False
                    if arr[i][j] != 1: one_stamp = False
            if zero_stamp is True or one_stamp is True:
                for i in range(x, x+N):
                    for j in range(y, y+N):
                        arr[i][j] = '-'
            result[0], result[1] = result[0]+zero_stamp, result[1]+one_stamp
    return arr, result
    
    
def solution(arr):
    answer = [0, 0]
    # 0과 1개수 세기
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0: answer[0] += 1
            if arr[i][j] == 1: answer[1] += 1
    # 스탬프 찍어보기
    stamp_size = len(arr)
    while stamp_size > 1:
        arr, tmp = QuadStamp(arr, stamp_size)
        answer[0] -= tmp[0] * (stamp_size**2 - 1)
        answer[1] -= tmp[1] * (stamp_size**2 - 1)
        stamp_size //= 2
    return answer