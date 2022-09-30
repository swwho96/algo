'''dictionary를 활용한 풀이'''
def solution(phone_book):
    phone_dict = {number : number for number in phone_book}
    for phone_num in phone_book:
        for i in range(1,len(phone_num)):
            if phone_num[:i] in phone_dict and phone_dict[phone_num[:i]] != phone_num:
                return False
    return True

'''startwith()를 활용한 풀이'''
def solution(phone_book):
    phone_book = sorted(phone_book)
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startwith(num2):
            return False
    return True