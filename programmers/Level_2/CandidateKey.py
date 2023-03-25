'''
키로 선택한 컬럼은 중복값이 없어야 한다. -> set() == len(rows)
두 컬럼 이상으로 조합했을 경우, 최소한의 컬럼으로 만들어야 한다.
'''
from itertools import combinations
def solution(relation):
    answer = set()
    n = len(relation)
    # 컬럼 조합 구하기
    combi = []
    cols = [i for i in range(len(relation[0]))]
    for i in range(1,len(relation[0])+1):
        combi.extend(combinations(cols, i))
    # 컬럼 조합이 row 수와 같다면 후보키 가능
    for c in combi:
        tmp_col = [''] * n
        for i in c:
            for idx, r in enumerate(relation):
                tmp_col[idx] += r[i]
        if len(set(tmp_col)) == n:
            # 최소성을 만족한다면 후보키 확정
            for a in answer:
                if set(a).issubset(set(c)):
                    break
            else:
                answer.add(c)
    
    return len(answer)