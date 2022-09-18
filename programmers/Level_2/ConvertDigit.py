def isPrimeNumber(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def convert(n, k):
    converted_number = []
    while n != 0:
        converted_number.append(str(n % k))
        n = n//k
    return ''.join(converted_number[::-1])

def solution(n, k):
    answer = 0
    k_number = convert(n,k)
    prime_candidate = k_number.split('0')
    print(prime_candidate)
    for p in prime_candidate:
        if p != '1' and p != '':
            if isPrimeNumber(int(p)) is True:
                answer += 1
    return answer