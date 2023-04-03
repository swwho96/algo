def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            tmp = stack.pop()
            answer[tmp] = i - tmp
        stack.append(i)
    for i in stack:
        answer[i] = (len(prices)-1) - i
    return answer