def solution(number, k):
    answer = ''
    while k >= 0:
        max_num = 0
        if k == 0 or len(number) == 1:
            answer += number
            break
        for i in range(len(number[:k+1])):
            if number[:k+1][i] == '9':
                start_cur = i
                break
            if max_num < int(number[:k+1][i]):
                max_num = int(number[:k+1][i])
                start_cur = i
        if start_cur == 0:
            answer += number[0]
            start_cur += 1
        else:
            k -= start_cur
        number = number[start_cur:]
    if k != 0:
        return answer[:-1]
    return answer


'''stack을 활용한 풀이'''
def solution(number, k):
    max_num = []
    for num in number:
        while max_num and max_num[-1] < num and k > 0:
            max_num.pop()
            k -= 1
        max_num.append(num)
    if k != 0:
        max_num = max_num[:-1]
    return ''.join(max_num)