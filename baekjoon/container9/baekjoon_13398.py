import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
mini = 0
dp = [0]
if N == 0:
    print(nums[-1])
else:
    for num in nums:
        if num > 0:
            dp.append(max(dp[-1]+num, num))
        else:
            if mini > num:
                dp.append(dp[-1]+mini)
                mini = num
            else:
                dp.append(dp[-1]+num)

print(max(dp))