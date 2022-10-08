from bisect import bisect_right

def solution(A, B):
    win = 0
    B = sorted(B)
    for a in A:
        next_player = bisect_right(B, a)
        if next_player < len(B):
            win += 1
            B.pop(next_player) # 게임을 이길 수 있을 경우
        else:
            B.pop(0) # 게임을 이길 수 없을 경우
    return win


# list 정렬 방식
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer