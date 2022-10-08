from collections import Counter
N = int(input())
num_card = list(map(int, input().split()))
card_cnt = Counter(num_card)
M = int(input())
numbers = list(map(int, input().split()))
for num in numbers:
    print(card_cnt[num], end=' ')