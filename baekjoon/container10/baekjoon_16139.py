import sys
input = sys.stdin.readline

S = input().rstrip()
question_cnt = int(input().rstrip())
dp = [[0] * (len(S)+1) for _ in range(26)]

# 사용된 알파벳 set
alpha_set = set(list(S))

# 24개 알파벳 별 누적합 계산
for i in range(26):
    for j in range(1, len(S)+1):
        dp[i][j] = dp[i][j-1] + (S[j-1] == chr(i+97))

for _ in range(question_cnt):
    alpha, l, r = input().split()
    if alpha in alpha_set:
        l, r = int(l), int(r)
        alpha_idx = ord(alpha) - 97
        print(dp[alpha_idx][r+1] - dp[alpha_idx][l])
    else:
        print(0)


'''
다른 방법의 dp 구현이지만, 메모리가 보다 효율적
'''
S = input().rstrip()
question_cnt = int(input().rstrip())
dp = [[0] * 26]
for i, s in enumerate(S):
    tmp = dp[i].copy()
    tmp[ord(s)-97] += 1
    dp.append(tmp)

for _ in range(question_cnt):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    alpha_idx = ord(alpha) - 97
    print(dp[r+1][alpha_idx] - dp[l][alpha_idx])

