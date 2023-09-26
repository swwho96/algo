def solution(num):
    cnt = 0
    while num != 1:
        cnt += 1
        if cnt == 500:
            return -1
        elif num % 2 == 0:
            num = num / 2
        else:
            num = num*3 + 1
    return cnt

# ---------------------------------

def Collatz(num, cnt):
    if num == 1:
        return cnt if cnt <= 500 else -1
    return Collatz(num // 2, cnt + 1) if num % 2 == 0 else Collatz(num * 3 + 1, cnt + 1)

def solution(num):
    return Collatz(num, 0)