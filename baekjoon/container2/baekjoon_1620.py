import sys
N, M = map(int, sys.stdin.readline().split())
pokatmon_dict = {}
# 포켓몬 도감 생성
for i in range(1,N+1):
    name = sys.stdin.readline().rstrip()
    pokatmon_dict[name] = i 
    pokatmon_dict[str(i)] = name
# 문제
for i in range(M):
    question = sys.stdin.readline().rstrip()
    print(pokatmon_dict[question])