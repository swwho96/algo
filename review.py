'''
블루레이의 크기를 줄여가면서, 해당 크기의 블루레이로 만든 동영상의 개수가 M개를 넘지 않는 경우를 구한다
'''

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
videos = list(map(int, input().split()))
start, end = max(videos), sum(videos)


while start <= end:
    size = (start+end) // 2
    # 블루레이 만들기
    blueray_cnt = 0
    tmp_sum = 0
    for i in range(N):
        if tmp_sum+videos[i] <= size:
            tmp_sum += videos[i]
        elif tmp_sum+videos[i] > size:
            tmp_sum = videos[i]
            blueray_cnt += 1
    if tmp_sum > 0: blueray_cnt += 1
    # 블루레이 확인
    if blueray_cnt > M:
        start = size + 1
    elif blueray_cnt <= M:
        end = size - 1

print(start)