from bisect import bisect_left
n = int(input())
needs = list(map(int, input().split()))
total = int(input())
min_tax, max_tax = 0, max(needs)
if sum(needs) <= total:
    print(max(needs))
else:
    while min_tax <= max_tax:
        tmp = 0
        mid = (min_tax+max_tax) // 2
        for i in needs:
            tmp += min(i, mid)
        if tmp > total:
            max_tax = mid - 1
        else:
            min_tax = mid + 1
    print(min(max(needs), max_tax))