# Counter는 해당 값과 값의 개수를 key-value로 하는 dict를 반환한다.

from collections import Counter
def solution(participant, completion):
    participant_dict = Counter(participant)
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict[c] == 0:
            del participant_dict[c]
    return participant_dict.keys()