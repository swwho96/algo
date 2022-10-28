N = int(input())
answer = 1
for i in range(1,N+1):
    answer *= i
cnt = 0
idx = len(str(answer)) - 1
while True:
    tmp = str(answer)[idx]
    if tmp != '0':
        print(cnt)
        break
    else:
        cnt += 1
        idx -= 1