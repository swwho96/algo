from bisect import bisect_left

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
number_to_find = list(map(int, input().split()))

numbers.sort()
for i in number_to_find:
    idx = bisect_left(numbers, i)
    if idx < len(numbers) and numbers[idx] == i:
        print(1)
    else:
        print(0)
