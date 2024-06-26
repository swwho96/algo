N, M = map(int, input().split())

def make(s:list, length:int):
    if length == M:
        print(' '.join(s))
        return
    for i in range(1, N+1):
        make(s+[str(i)], length+1)

make([], 0)        