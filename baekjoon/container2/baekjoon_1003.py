import sys
T = int(sys.stdin.readline().rstrip())
zero_cnt = [1, 0]
one_cnt = [0, 1]
for i in range(2, 41):
    zero_cnt += [zero_cnt[i-1] + zero_cnt[i-2]]
    one_cnt += [one_cnt[i-1] + one_cnt[i-2]]

for _ in range(T):
    num = int(sys.stdin.readline().rstrip())
    print(zero_cnt[num], one_cnt[num])