# 완전탐색 O(n^2)
def solution1(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        now_price = prices[i]
        for j in range(i+1, len(prices)):
            if now_price > prices[j]:
                answer[i] += 1
                break
            else:
                answer[i] += 1 
    return answer


# 스택
def solution2(prices):
    answer = [0]*len(prices)
    s = []
    
    for i, p in enumerate(prices):
        while s and prices[s[-1]] > p:
            j = s.pop()
            answer[j] = i-j            
        s.append(i)
    
    while s:
        i = s.pop()
        answer[i] = len(prices)-1-i
    
    return answer