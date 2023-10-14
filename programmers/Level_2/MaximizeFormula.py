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


# --------------------------------------------------------------------------------------

from itertools import permutations
import re

def toPostFix(tokens, priorty):
    stack = []
    postfix = []
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        else:
            if not stack:
                stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

def calc(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue

        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(eval(num1 + token + num2))
    return stack.pop()

def solution(expression):
    tokens = re.split(r'([-+*/()])|\s+', expression)
    operators = ['+', '-', '*']
    answer = 0

    for i in map(list, permutations(operators)):
        priority = {o:p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))

    return answer