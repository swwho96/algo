N = int(input())
if N == 1:
        print(0)
else:
    # 소수 구하기
    primeNum_checklist = [False, False] + [True] * (N-1)
    primeNum = []
    for i in range(2, N+1):
        if primeNum_checklist[i] == True:
            primeNum.append(i)
            for j in range(i*i, N+1, i):
                primeNum_checklist[j] = False
    # 연속된 합 구하기
    left, right, result = 0, 0, 0
    total = primeNum[left]
    while left<=right<len(primeNum):
        if total == N: # 같으면 경우의수 +1
            result += 1
            total -= primeNum[left]
            left += 1
        elif total < N: # 작으면 오른쪽 하나 더하고1
            right += 1
            if right >= len(primeNum):
                break
            total += primeNum[right]
        else: # 크면 왼쪽 하나 빼고
            total -= primeNum[left]
            left += 1
            if left >= len(primeNum):
                break
    print(result)