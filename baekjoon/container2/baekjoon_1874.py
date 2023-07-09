# import sys
# n = int(sys.stdin.readline().rstrip())
# num = []
# result = []
# push_and_pop = []
# for _ in range(n):
#     num.append(int(sys.stdin.readline().rstrip()))

# num = num[::-1]
# start = num[-1]
# max = start
# for i in range(1, start+1):
#     result.append(i)
#     push_and_pop.append('+')

# while True:
#     if len(result) <= 0:
#         if len(num) <= 0:
#             break
#         else:
#             for i in range(max+1, num[-1]+1):
#                 result.append(i)
#                 push_and_pop.append('+')
#             max = num[-1]
#     if len(num) <= 0:
#         push_and_pop = ['NO']
#         break
#     if num[-1] >= result[-1]:
#         for i in range(max+1, num[-1]+1):
#             result.append(i)
#             push_and_pop.append('+')
#         if max < num[-1]: max = num[-1]
#     else:
#         push_and_pop = ['NO']
#         break
#     num.pop()
#     result.pop()
#     push_and_pop.append('-')

# for i in push_and_pop:
#     print(i)

import sys
input = sys.stdin.readline
n = int(input())
result = []
tmp_stack = []
stack = []
k, idx = 1, 0
for _ in range(n):
    stack.append(int(input()))

while idx <= n-1:
    now = stack[idx]
    if not tmp_stack or now > tmp_stack[-1]:
        result.append('+')
        tmp_stack.append(k)
        k += 1
    elif now == tmp_stack[-1]:
        result.append('-')
        tmp_stack.pop()
        idx += 1
    else:
        result = 'NO'
        break

if result != 'NO':
    for r in result:
        print(r)
else:
    print(result)