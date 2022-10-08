N = int(input())
for _ in range(N):
    ps = input()
    answer = 0
    for char in ps:
        if answer < 0:
            break
        if char == '(':
            answer += 1
        else:
            answer -= 1
    print('YES') if answer == 0 else print('NO')