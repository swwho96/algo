L = int(input())
word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
H = 0
for i in range(L):
    hash_key = alpha.index(word[i]) + 1
    H += hash_key * (31 ** i)
print(H % 1234567891)
