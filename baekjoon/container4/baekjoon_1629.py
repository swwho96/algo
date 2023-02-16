a, b, c = map(int, input().split())
print(pow(a,b,c))

# ________________________________________

a, b, c = map(int, input().split())

def rest_num(a,b,c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (rest_num(a, b//2, c) ** 2) % c
    else:
        return ((rest_num(a, b//2, c) ** 2) * a) % c

print(rest_num(a,b,c))