N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
answer = [] # 출력 문자열 생성
cursor = 0 # 현재 위치
for _ in range(N):
    cursor = (cursor+K-1) % len(nums)
    tmp = nums.pop(cursor)
    answer.append(tmp)
print("<"+', '.join(map(str, answer))+">")