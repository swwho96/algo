def solution(n):
    def move(start, to):
        answer.append([start, to])

    def hanoi(N, start, to, via):
        if N == 1:
            move(start, to)
        else:
            hanoi(N-1, start, via, to)
            move(start, to)
            hanoi(N-1, via, to, start)
            
    answer = []
    hanoi(n, 1, 3, 2)
    return answer