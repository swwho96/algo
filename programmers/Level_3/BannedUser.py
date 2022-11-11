from itertools import permutations

def IdCheck(uid, bid):
    if len(uid) != len(bid):
        return False
    correct_cnt = 0
    for i in range(len(bid)):
        if bid[i] == uid[i] or bid[i] == '*':
            correct_cnt += 1
    return True if correct_cnt == len(bid) else False
    
def solution(user_id, banned_id):
    answer = set()
    for id_list in permutations(user_id, len(banned_id)):
        for uid, bid in zip(id_list, banned_id):
            flag = 1
            if IdCheck(uid, bid) is False:
                flag = 0
                break
        if flag == 1:
            id_list = tuple(sorted(id_list))
            answer.add(id_list)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


# import re
# from itertools import permutations

# def solution(user_id, banned_id):
#     ban = ' '.join(banned_id).replace('*','.')
#     answer = set()
#     for id_list in permutations(user_id, len(banned_id)):
#         if re.fullmatch(ban, ' '.join(id_list)):
#             answer.add(''.join(sorted(id_list)))
#     return len(answer)