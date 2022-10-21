from collections import deque
N, K = map(int, input().split())
onepan = deque('?'*N)
check = []
for i in range(K):
    S, alpha = input().split()
    onepan.rotate(int(S))
    if (onepan[0] != '?') and (onepan[0] != alpha):
        onepan = '!'
        break
    elif (onepan[0] == '?') and (alpha in onepan):
        onepan = '!'
        break
    else:
        onepan[0] = alpha

answer = ''.join(onepan)
print(answer)
