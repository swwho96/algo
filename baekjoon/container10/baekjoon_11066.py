import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    K = int(input().rstrip())
    files = list(map(int, input().split()))

    # 부분합 계산
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i-1] + files[i-1]

    # DP 배열 초기화
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    opt = [[0] * (K + 1) for _ in range(K + 1)]  # 최적 k 값을 저장하는 배열

    # 초기 조건 설정
    for i in range(1, K + 1):
        opt[i][i] = i

    # DP 계산 및 최적화 적용
    for length in range(2, K + 1):  # 부분 파일의 길이
        for i in range(1, K + 2 - length):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # opt[i][j-1] <= k <= opt[i+1][j] 범위를 보장
            for k in range(opt[i][j-1], min(opt[i+1][j] + 1, j)):
                cost = dp[i][k] + dp[k+1][j] + prefix_sum[j] - prefix_sum[i-1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    opt[i][j] = k  # 최적 k 업데이트

    # 최종 결과 출력
    print(dp[1][K])