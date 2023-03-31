# 여러 종류에서 몇가지를 고르는 경우의 수는
# (각 개수 + 1)를 모두 곱하고 -1 (적어도 하나는 골라야 하므로)하여 구한다

def solution(clothes):
    answer = 1
    closet = {}
    for _, kind in clothes:
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 1
    for kinds in closet.values():
        answer *= kinds+1
    return answer - 1