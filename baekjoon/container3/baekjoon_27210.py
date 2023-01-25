n = int(input())
lst = list(map(int, input().split()))

lst2 = [0]
window_sum = 0
for i in range(n):
    if lst[i] == 1:
        window_sum += 1
    else:
        window_sum -= 1
    lst2.append(window_sum)

lst2.sort()
print(lst2[-1] - lst2[0])