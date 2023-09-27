from itertools import product
def solution(word):
    alpha = ['A','E','I','O','U']
    dictionary = []
    for i in range(1,6):
        dictionary += [''.join(w) for w in product(alpha, repeat=i)]
    dictionary = sorted(dictionary)
    return dictionary.index(word)+1

# --------------------------------------------------------------------

def solution(word):
    def dictionary(s:str):
        if len(s) >= 5:
            return
        for i in ['A', 'E', 'I', 'O', 'U']:
            answer.append(s+i)
            dictionary(s+i)
            
    answer = []
    dictionary('')
    return answer.index(word) + 1