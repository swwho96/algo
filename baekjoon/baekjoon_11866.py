# 요세푸스 문제 0
N, K = map(int, input().split())
people = [i for i in range(1, N+1)]
start = 0
result = '<'
while len(people) > 1:
    start += K-1
    if start >= len(people):
        start = start % len(people)
    result += str(people.pop(start)) + ', '

print(result + str(people.pop()) + '>')