import re
from itertools import permutations

def solution(user_id, banned_id):
    ban = ' '.join(banned_id).replace('*','.')
    answer = set()
    for id_list in permutations(user_id, len(banned_id)):
        if re.fullmatch(ban, ' '.join(id_list)):
            answer.add(''.join(sorted(id_list)))
    return len(answer)