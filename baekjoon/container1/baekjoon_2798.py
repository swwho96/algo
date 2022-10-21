N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = []
sorted(cards, reverse=True)

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if (cards[a] + cards[b] + cards[c]) > M:
                continue
            else:
                answer.append(cards[a] + cards[b] + cards[c])

print(max(answer))
