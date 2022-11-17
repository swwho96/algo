# def solution(jobs):
#     answer = 0
#     n = len(jobs)
#     jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
#     cur_time, task_time = jobs.pop(0)
#     total_time = task_time
#     cur_time += task_time
#     while jobs:
#         for i in range(len(jobs)):
#             if jobs[i][0] <= cur_time and task_time >= jobs[i][1]:
#                 task_time = jobs[i][1]
#             else:
#                 if jobs[i-1][0] > cur_time:
#                     total_time += jobs[i][1]
#                 else:
#                     total_time += (cur_time - jobs[i-1][0]) + jobs[i-1][1]
#                 cur_time += jobs[i-1][1]
#                 jobs.pop(i-1)
#                 break
#     return (total_time) // n

import heapq
def solution(jobs):
    n = len(jobs)
    total_task_time = 0
    current_time = 0
    q = []
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    while jobs or q:
        # 현재 수행 가능한 작업 q에 등록
        while jobs and jobs[0][0] <= current_time:
            j = jobs.pop(0)
            heapq.heappush(q, [j[1],j[0]])
        # q에 등록된 작업 수행
        if q:
            needed_time, register_time = heapq.heappop(q)
            total_task_time += (current_time - register_time) + needed_time
            current_time += needed_time
        else:
            current_time += 1
    return total_task_time // n