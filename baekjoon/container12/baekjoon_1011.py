def alpha_centauri(x, y):
    distance = y - x
    move = 0
    step = 1
    total_moved = 0

    while total_moved < distance:
        move += 1
        total_moved += step
        if move % 2 == 0:  # 짝수일 때 이동 거리 증가
            step += 1

    return move

# 테스트 케이스 입력 및 출력
t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    x, y = map(int, input().split())
    print(alpha_centauri(x, y))