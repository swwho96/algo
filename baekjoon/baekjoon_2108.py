from collections import Counter
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
c = Counter(numbers)
c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
print(round(sum(numbers) / N))
print(sorted(numbers)[int(N/2)])
if len(c) <= 1:
    print(c[0][0])
elif c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(max(numbers)-min(numbers))