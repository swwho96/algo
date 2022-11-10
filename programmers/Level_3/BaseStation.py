def solution(n, stations, w):
    wide = 2*w+1
    answer = 0
    non_connect_area = []
    non_connect_area.append(stations[0] - w - 1)
    
    for i in range(1, len(stations)):
        non_connect_area.append((stations[i]-w-1) - (stations[i-1]+w))
    if stations[-1] < n:
        non_connect_area.append(n - (stations[-1]+w))
    print(non_connect_area)
    for area in non_connect_area:
        answer += (area-1) // wide + 1
    return answer