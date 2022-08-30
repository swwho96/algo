from itertools import permutations
def solution(numbers):
    answer = 0
    # numbers로 가능한 숫자 조합 만들기
    number_permut = set()
    for i in range(1, len(numbers)+1):
        number_permut |= set(map(int, map(''.join, (permutations(list(numbers),i)))))
    
    # numbers 조합 중 가장 큰 수까지 prime number 구하기
    primeNum = [False, False] + [True for i in range(2, max(number_permut)+1)]
    for i in range(2, max(number_permut)+1):
        if primeNum[i] is True:
            for j in range(i*i, max(number_permut)+1, i):
                primeNum[j] = False
    
    # numbers 조합 중 소수 개수 구하기
    for num in number_permut:
        if primeNum[num] is True:
            answer += 1
            
    return answer