import sys
T = int(sys.stdin.readline().rstrip())
wave_numbers = [1,1,1,2,2]
for i in range(4, 101):
    wave_numbers += [wave_numbers[i] + wave_numbers[i-4]]
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(wave_numbers[n-1])