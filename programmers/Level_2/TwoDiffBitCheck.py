'''x와 x보다 큰 수의 bin값을 하나하나 비교하는 방법'''

def bit_checker(x:str, y:str)->bool:
    answer = 0
    for x_bit, y_bit in zip(x,y):
        if answer > 2:
            return False
        else:
            if x_bit != y_bit:
                answer += 1
    return True if answer <= 2 else False
            

def solution(numbers):
    answer = []
    for num in numbers:
        x = format(num,'b')[::-1]
        y = num + 1
        while True:
            y_to_bit = format(int(y), 'b')
            x += '0' * (len(str(y_to_bit)) - len(str(x)))
            if bit_checker(x[::-1], y_to_bit) is True:
                answer.append(int(y_to_bit, 2))
                break
            y += 1
    return answer


'''x보다 큰 가장 작은 수를 만드는 방법'''

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            num_to_bin = '0' + bin(num)[2:]
            first_zero_index = num_to_bin.rfind('0')
            num_to_bin = list(num_to_bin)
            num_to_bin[first_zero_index] = '1'
            num_to_bin[first_zero_index+1] = '0'
            answer.append(int(''.join(num_to_bin), 2))
    return answer