import sys

T = int(sys.stdin.readline())
test_cases = []

# 테스트 케이스 입력
for _ in range(T):
    test_cases.append(int(sys.stdin.readline().rstrip()))

max_test_case = max(test_cases)

# 소수 찾기
prime_number = [False, False] + [True for _ in range(max_test_case+1)]
for i in range(2, max_test_case+1):
    if prime_number[i] is True:
        for j in range(i*i, max_test_case+1, i):
            prime_number[j] = False

for case in test_cases:
    x, y = case//2, case//2
    while True:
        if prime_number[x] is True and prime_number[y] is True:
            print(x, y)
            break
        else:
            x -= 1
            y += 1
