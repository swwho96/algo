'''
문자열을 주어진 크기만큼 확인하면서, 각 알파벳별 개수를 만족하면 개수를 세어 더한다
'''

import sys
input = sys.stdin.readline
S, T = map(int, input().split())
string = input().rstrip()
minimum_cnt = list(map(int, input().split())) # [A, C, G, T]
minimum_dict = {k:v for k, v in zip(['A', 'C', 'G', 'T'], minimum_cnt)}
left, right = 0, 0

result = 0
window = {'A':0, 'C':0, 'G':0, 'T':0}
window[string[left]] += 1
while right < S:
    if right-left+1 == T:
        if window['A'] >= minimum_dict['A'] and window['C'] >= minimum_dict['C'] and window['G'] >= minimum_dict['G'] and window['T'] >= minimum_dict['T']:
            result += 1
        window[string[left]] -= 1
        left += 1
        if right == S-1:
            break
        right += 1
        window[string[right]] += 1
    else:
        right += 1
        window[string[right]] += 1
print(result)