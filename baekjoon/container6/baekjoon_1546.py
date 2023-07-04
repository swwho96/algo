n = int(input())
grades = list(map(int, input().split()))
print(sum(grades) * 100 / max(grades) / n)