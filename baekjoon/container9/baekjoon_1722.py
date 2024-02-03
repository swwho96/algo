import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

cases = []
for i in range(N, -1, -1):
    cases.append(factorial(i))
numbers = [i for i in range(1, N+1)]
tmp = list(map(int, input().split()))
op = tmp.pop(0)
if op == 1:
    k = tmp[-1] # k번째 수열
    result = [] # 결과 배열 정의
    for i in range(1, N): # 첫 자리부터 마지막 자리까지
        if cases[i] >= k:
            idx = 0
        else:
            idx = k // cases[i] - 1 if k % cases[i] == 0 else k // cases[i]
            k -= (idx) * cases[i]
        next_number = numbers[idx]
        result.append(next_number)
        numbers.remove(next_number)
    result.append(numbers[-1])
    print(' '.join(map(str, result)))
elif op == 2:
    k = 1
    for i, n in enumerate(tmp, start=1):
        if n == numbers[0]:
            numbers.remove(n)
        else:
            idx = numbers.index(n)
            k += idx * cases[i]
            numbers.remove(n)
    print(k)