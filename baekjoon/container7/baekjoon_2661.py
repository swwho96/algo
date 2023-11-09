N = int(input())
numbers = int('3'*80)

def check(num):
    for i in range(len(num)):
        for j in range(1, (len(num)-i)//2 + 1):
            if num[i:i+j] == num[i+j:i+j+j]:
                return False
    return True

def bfs(result):
    global numbers
    if len(result) == N and check(result):
        numbers = min(numbers, int(result))
        print(numbers)
        exit()
    for i in ['1','2','3']:
        tmp = ''.join([result, i])
        if check(tmp):
            bfs(tmp)

bfs('')