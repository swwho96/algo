from collections import defaultdict
def solution(tickets):
    answer = []
    # ticket 도착지 내림차순 정렬
    tickets = sorted(tickets, key=lambda x: x[1], reverse=True)
    # 티켓 그래프 생성
    tickets_dict = defaultdict(list)
    for t in tickets:
        tickets_dict[t[0]].append(t[1])
    # dfs
    stack = ['ICN']
    while stack:
        start = stack.pop()
        if not tickets_dict[start]:
            answer.append(start)
        else:
            stack.append(start)
            stack.append(tickets_dict[start].pop())
    return answer[::-1]