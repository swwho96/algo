from itertools import permutations
def solution(expression):
    answer = []
    used_expression = []
    expression_list = []
    # 사용된 연산자 종류 구하기
    for ex in ['*', '+', '-']:
        if ex in expression:
            used_expression.append(ex)
    # 수식 리스트화
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            expression_list.extend([tmp, e])
            tmp = ''
    expression_list.append(tmp)
    # 연산자 우선순위 조합 구하기
    expression_combi = permutations(used_expression, len(used_expression))
    # 각 우선순위 조합 별 계산 결과 구하기
    for combi in expression_combi:
        temp = expression_list.copy()
        for operator in combi:
            while operator in temp:
                idx = temp.index(operator)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        answer.append(abs(int(temp[0])))
    return max(answer)