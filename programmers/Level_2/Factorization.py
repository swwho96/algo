from collections import Counter

def factorization(x):
    div = 2
    fact_numbers = []
    while div <= x:
        if x % div == 0:
            fact_numbers.append(div)
            x /= div
        else:
            div += 1
    return Counter(fact_numbers)

def solution(arr):
    result = 1
    factorization_set = Counter()
    # 지수들의 합집합
    for num in arr:
        factorization_set = (factorization_set | factorization(num))
    # 모든 지수들의 곱
    for num, repetition in dict(factorization_set).items():
        for _ in range(repetition):
            result *= num
    return result