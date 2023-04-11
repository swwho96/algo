n = int(input())
liquer = list(map(int, input().split()))
liquer.sort()
result = int(1e10)
s, e = 0, n-1
final_s, final_e = s, e
while s<e:
    tmp = (liquer[s]+liquer[e])
    if abs(result) > abs(tmp):
        result = tmp
        final_s, final_e = s, e
    if tmp > 0:
        e -= 1
    elif tmp < 0:
        s += 1
    else:
        break
print(liquer[final_s], liquer[final_e])