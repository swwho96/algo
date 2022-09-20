from collections import defaultdict
def solution(msg):
    default_dict = {word: idx+1 for idx, word in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    last_idx = 26
    answer = []
    left, right = 0, 1
    while left <= len(msg)-1:
        current_input = msg[left:right]
        while True:
            if msg[left:right] in default_dict:
                if right > len(msg)-1:
                    answer.append(default_dict[current_input])
                    return answer
                else:
                    right += 1
                    current_input = msg[left:right]
            else:
                default_dict[current_input] = last_idx+1
                last_idx += 1
                answer.append(default_dict[msg[left:right-1]])
                left = right - 1
                right = left + 1
                break
    return answer