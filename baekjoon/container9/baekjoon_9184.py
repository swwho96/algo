while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    def w(a:int, b:int, c:int)->int:
        if a <= 0 or b <= 0 or c <= 0:
            return 1

        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)

        elif dp[a][b][c]:
            return dp[a][b][c]

        elif a < b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]

        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dp[a][b][c]
        
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')