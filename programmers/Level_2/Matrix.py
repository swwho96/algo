'''
첫 행부터 차례대로 계산해 answer에 담는 행렬 곱 계산 방식
'''

def solution(arr1, arr2):
    answer = []
    for a in arr1:
        row_result = []
        for i in range(len(arr2[0])):
            tmp = []
            for b in arr2:
                tmp += [b[i]]
            row_result.append(sum([x*y for x,y in zip(a, tmp)]))
        answer.append(row_result)
    return answer


'''
행과 열을 바꾸어 계산하는 방식
'''

def solution(arr1, arr2):
    answer = []
    for a in arr1:
        tmp = []
        for b in list(zip(*arr2)):
            tmp.append(sum([x*y for x,y in zip(a,b)]))
        answer.append(tmp)
    return answer