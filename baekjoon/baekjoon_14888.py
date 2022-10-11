def bfs(idx, numbers, math_expression, plus, minus, multiple, divide):
    if plus == minus == multiple == divide == 0:
        global maximum, minimum
        maximum = max(maximum, math_expression)
        minimum = min(minimum, math_expression)
        return
    if plus > 0:
        bfs(idx+1, numbers, math_expression + numbers[idx], plus-1, minus, multiple, divide)
    if minus > 0:
        bfs(idx+1, numbers, math_expression - numbers[idx], plus, minus-1, multiple, divide)
    if multiple > 0:
        bfs(idx+1, numbers, math_expression * numbers[idx], plus, minus, multiple-1, divide)
    if divide > 0:
        bfs(idx+1, numbers, int(math_expression / numbers[idx]), plus, minus, multiple, divide-1)


N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
maximum = -10e9
minimum = 10e9
bfs(1, numbers, numbers[0], plus, minus, multiple, divide)
print(maximum)
print(minimum)