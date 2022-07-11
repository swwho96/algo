'''
주어진 문자열을 기준에 맞게 정렬하여 반환하는 문제
'''

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_log, digit_log = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_log + digit_log