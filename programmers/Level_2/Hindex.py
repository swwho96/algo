def solution(citations):
    answer = 0
    citations_sort = citations.sort(reverse=True)
    for i, c in zip(range(1, len(citations)+1), citations):
        if c <= i:
            break
        else:
            answer = i
    return answer