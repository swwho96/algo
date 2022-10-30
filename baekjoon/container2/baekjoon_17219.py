import sys
N, M = map(int, sys.stdin.readline().split())
password_dict = {}
a = sys.stdin.read().splitlines()
sites = a[-M:]
password_dict = dict(p.split() for p in a[:-M])
for s in sites:
    print(password_dict[s])