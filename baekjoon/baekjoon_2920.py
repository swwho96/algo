melody = list(map(int, input().split()))
melody_ordered = [i for i in range(1, 9)]

if melody == melody_ordered:
    print('ascending')
elif melody == sorted(melody_ordered, reverse=True):
    print('descending')
else:
    print('mixed')
