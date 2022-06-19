def hanoi(n, col1, col3, col2):
    if n == 1:
        print(col1, col3)
    else:
        hanoi(n-1, col1, col2, col3)
        print(col1, col3)
        hanoi(n-1, col2, col3, col1)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)