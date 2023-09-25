def solution(s):
    try:
        int(s)
        return True if len(s) in [4,6] else False
    except:
        return False

import re
def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))

def solution(s):
    return bool(len(s) in [4,6] and s.isdecimal())