# N, M = map(int, input().split())

# def make_num(nums:list, check:set):
#     if len(nums) == M:
#         print(' '.join(nums))
#         return
#     for i in range(1, N+1):
#         if str(i) not in check:
#             make_num(nums+[str(i)], check|set(str(i)))

# make_num([], set())

N, M = map(int, input().split())

def make_num(nums:list, check:set):
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return
    for i in range(1, N+1):
        if i not in check:
            make_num(nums+[i], check|set([i]))

make_num([], set())