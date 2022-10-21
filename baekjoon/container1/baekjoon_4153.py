while True:
    three_lines = list(map(int, input().split()))
    if three_lines == [0, 0, 0]:
        break
    else:
        three_lines = sorted(three_lines, reverse=True)
        if (three_lines[0] ** 2) == (three_lines[1] ** 2 + three_lines[2] ** 2):
            print('right')
        else:
            print('wrong')
