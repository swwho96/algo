for i in range(1000000):
    N = str(i)
    counter = {str(i):0 for i in range(10)}
    for n in N:
        counter[n] += 1
    # print(max(max(counter[c] for c in '01234578'), (counter['9']+counter['6']+1)//2))
    tmp = max(max(counter[c] for c in '01234578'), (counter['9']+counter['6']+1)//2)