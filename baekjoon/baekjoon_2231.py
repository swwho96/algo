N = input()
maked_number = 1000001
for i in range(1, int(N)+1):
    answer = 0
    for j in range(len(str(i))):
        answer += int(str(i)[j])
    answer += int(i)
    if answer == int(N) and maked_number > answer:
        maked_number = int(i)

print(maked_number if maked_number != 1000001 else 0)