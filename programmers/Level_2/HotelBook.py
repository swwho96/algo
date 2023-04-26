from collections import deque
def solution(book_time):
    answer = 0
    hotel = deque([])
    # 예약시간 분으로 변경
    for i in range(len(book_time)):
        check_in = list(map(int, book_time[i][0].split(':')))
        book_time[i][0] = check_in[0] * 60 + check_in[1]
        check_out = list(map(int, book_time[i][1].split(':')))
        book_time[i][1] = check_out[0] * 60 + check_out[1]
        
    # 체크인이 빠른 순서대로 예약 정렬
    book_time = sorted(book_time, key=lambda x: x[0])
    for customer in book_time:
        tmp = []
        for room in hotel:
            if room[-1]+10 > customer[0]:
                tmp.append(room)
        tmp.append(customer)
        hotel = tmp
        answer = max(answer, len(hotel))
    return answer