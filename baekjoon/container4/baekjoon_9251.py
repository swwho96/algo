a = input()
b = input()
check = [[0] * (len(a)+1) for _ in range(len(b)+1)]
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] != a[j-1]:
            check[i][j] += max(check[i][j-1], check[i-1][j])
        else:
            check[i][j] = check[i-1][j-1] + 1

i, j = len(b), len(a)
tmp = ''
result = []
while i>=0 and j>=0:
    if check[i][j] == check[i][j-1]:
        i, j = i, j-1
    elif check[i][j] == check[i-1][j]:
        i, j = i-1, j
    else:
        print(a[j-1], b[i-1])
        result.append(a[j-1])
        i, j = i-1, j-1

print(len(result))