import sys
test_cases = []
max_n = 1

# 테스트 케이스 입력받기
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        test_cases.append(n)
        if n >= max_n:
            max_n = n

sosu = [False, False] + [True for _ in range(max_n*2+1)]

# 테스트 케이스 중 가장 큰 수까지 소수 찾기
for i in range(2, max_n*2+1):
    if sosu[i] == True:
        for j in range(i*2, max_n*2+1, i):
            sosu[j] = False

# 각 테스트 케이스 별 소수 개수 출력
for case in test_cases:
    cnt = 0
    for i in range(case+1, case*2+1):
        if sosu[i] == True:
            cnt+=1
    print(cnt)