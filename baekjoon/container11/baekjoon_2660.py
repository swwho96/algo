import sys
input = sys.stdin.readline

N = int(input().rstrip())
friends = [[float('inf')]*(N+1) for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    friends[a][b] = 1
    friends[b][a] = 1

# 플로이드-워셜 (모든 회원과의 거리 구하기)
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i!=j:
                friends[i][j] = min(friends[i][j], friends[i][k]+friends[k][j])
            else: friends[i][j] = 1

# 회장 후보 찾기 (점수가 가장 낮은 회원)
answer = [] # (회원번호, 점수)
lowest_score = N
for i in range(1, N+1):
    tmp_score = max(friends[i][1:])
    lowest_score = min(lowest_score, tmp_score)
    while answer and answer[-1][1] > lowest_score:
        answer.pop()
    answer.append((i, tmp_score))

while answer and answer[-1][1] > lowest_score:
    answer.pop()

# 출력 (회장후보의 점수와 후보수 / 회장후보의 회원번호 오름차순)
print(answer[-1][1], len(answer))
print(' '.join([str(i) for i, _ in answer]))