n = int(input())
how_to_make_n = [0, 0, 1, 1]
for i in range(4,n+1):
    if i % 3 == 0 and i % 2 == 0:
        how_to_make_n += [min(1+how_to_make_n[i-1], how_to_make_n[i//3] + 1, how_to_make_n[i//2] + 1)]
        continue
    if i % 3 == 0:
        how_to_make_n += [min(1+how_to_make_n[i-1], how_to_make_n[i//3] + 1)]
        continue
    if i % 2 == 0:
        how_to_make_n += [min(1+how_to_make_n[i-1], how_to_make_n[i//2] + 1)]
        continue
    how_to_make_n += [how_to_make_n[i-1] + 1]
print(how_to_make_n[n])