N = int(input())

nums = [0] + ([1] * 9)
for _ in range(N-1):
    new_nums = [0] * 10
    for idx, n in enumerate(nums):
        # 0의 개수 만큼 1이 늘어난다
        if idx == 0:
            new_nums[idx+1] += n
        # 9의 개수 만큼 8이 늘어난다
        elif idx == 9:
            new_nums[idx-1] += n
        # 다른 숫자들은 전부 +1 -1을 붙일 수 있다
        else:
            new_nums[idx+1] += n
            new_nums[idx-1] += n
    print(new_nums)
    nums = new_nums
print(sum(nums))