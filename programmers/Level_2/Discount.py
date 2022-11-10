from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_dict = {name:cnt for name, cnt in zip(want, number)}
    for i in range(0, len(discount)-9):
        flag = True
        tmp = dict(Counter(discount[i:i+10]))
        for k, v in want_dict.items():
            if k not in tmp.keys() or tmp[k] < v:
                flag = False
                break
        if flag is True: answer+=1
    return answer