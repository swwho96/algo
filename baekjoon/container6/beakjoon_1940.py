n = int(input())
m = int(input())
numbers = set(map(int, input().split()))
result_set = set()
result_cnt = 0
for num in numbers:
    if m > num and (m - num) in numbers:
        if num in result_set or m-num in result_set or num == m-num:
            continue
        else:
            result_cnt += 1
            result_set.add(num)
            result_set.add(m-num)
print(result_cnt)