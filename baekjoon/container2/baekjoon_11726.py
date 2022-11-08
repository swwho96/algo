n = int(input())
tiles = [1, 2, 3]
if n < 3:
    print(tiles[n-1] % 10007)
else:
    for i in range(3, n):
        tiles.append(tiles[-1] + tiles[-2])
    print(tiles[n-1] % 10007)