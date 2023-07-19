import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lessons = list(map(int, input().split()))
def make_blueray(maximum):
    global lessons
    blueray = 0
    tmp = 0
    for l in lessons:
        if tmp+l > maximum:
            blueray += 1
            tmp = l
        else:
            tmp += l
    return blueray

s, e = max(lessons), sum(lessons)
while s <= e:
    mid = (s + e) // 2
    blueray_cnt = make_blueray(mid)
    if m > blueray_cnt:
        e = mid - 1
    else:
        s = mid + 1
print(s)