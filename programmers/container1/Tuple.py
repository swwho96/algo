def solution(s):
    result = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for nums in s:
        nums = nums.split(',')
        for num in nums:
            if int(num) not in result:
                result.append(int(num))
    return result


# ---------------------------------------------------------------------------

def solution(s):
    answer = []
    # 원소 개수 별 정렬
    s = s[1:-1].replace('},{', '} {').split(' ')
    s = sorted(s, key= lambda x: len(x))
    s = ' '.join(s).replace('} {', ',').replace('{', '').replace('}', '')
    for i in s.split(','):
        if int(i) not in answer:
            answer.append(int(i))
    return answer