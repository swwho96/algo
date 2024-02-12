import sys
input = sys.stdin.readline

dp_0 = [0,0,1]
dp_1 = [0,1,0]

N = int(input())
if N <= 2:
    print(dp_0[N]+dp_1[N])
else:
    for _ in range(N-2):
        tmp_0 = dp_0[-1]+dp_1[-1]
        tmp_1 = dp_0[-1]
        dp_0.append(tmp_0)
        dp_1.append(tmp_1)
    print(dp_0[N]+dp_1[N])