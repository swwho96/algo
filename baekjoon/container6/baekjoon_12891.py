s, p = map(int, input().split())
dna = input()
index = {'A':0, 'C':1, 'G':2, 'T':3}
acgt = [0,0,0,0]
result = 0
password = list(map(int, input().split()))
for i in range(s):
    acgt[index[dna[i]]] += 1
    if i >= p-1:
        if acgt[0] >= password[0] and acgt[1] >= password[1] and acgt[2] >= password[2] and acgt[3] >= password[3]:
            result += 1
        acgt[index[dna[i-(p-1)]]] -= 1
print(result)