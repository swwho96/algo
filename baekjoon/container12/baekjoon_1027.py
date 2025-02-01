N = int(input())
buildings = list(map(int, input().split()))

# 현재 빌딩에서 목표 빌딩까지 직선 그래프를 그리고
# 중간 빌딩들의 x좌표를 넣어 그래프에 닿으면 볼 수 없다
can_look = [0] * N
for i, h in enumerate(buildings):
    tmp_can_look = 0
    for j in range(N):
        if i < j:
            for x in range(i+1, j):
                if ((buildings[j]-h) / (j-i))*(x-i) + h <= buildings[x]:
                    break
            else:
                tmp_can_look += 1
        elif i > j:
            for x in range(i-1, j, -1):
                if ((buildings[j]-h) / (j-i))*(x-i) + h <= buildings[x]:
                    break
            else:
                tmp_can_look += 1
    can_look[i] += tmp_can_look

print(max(can_look))