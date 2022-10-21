N = int(input())
out_time = list(map(int, input().split()))
out_time.sort()
waiting_time = []
for i in range(1, N+1):
    waiting_time.append(sum(out_time[:i]))

print(sum(waiting_time))