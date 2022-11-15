from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = Counter()
    for menu in orders:
        menu = sorted(menu)
        for i in course:
            if i > len(menu):
                break
            for j in combinations(menu, i):
                if len(''.join(j)) >= 2:
                    answer[''.join(j)] += 1

    answer = sorted(answer.items(), key=lambda x: (len(x[0]), x[1]), reverse=True)
    temp = [menu for menu in answer if menu[1] >= 2]

    if len(temp) < 1:
        return []
    result = [temp[0][0]]
    max_len = temp[0][1]

    for i in range(1,len(temp)):
        if len(temp[i][0]) == len(temp[i-1][0]):
            if temp[i][1] >= max_len:
                result.append(temp[i][0])
        elif temp[i][1] >= temp[i-1][1]:
            max_len = temp[i][1]
            result.append(temp[i][0])
    return sorted(result)

#---------------------------------------------------------------------------------------------------

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        print('most_ordered: ', most_ordered)
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]


print(solution(["ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE"], [2,3,5]))