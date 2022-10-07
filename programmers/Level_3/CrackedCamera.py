def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[0])
    while routes:
        camera_site = routes.pop()[0]
        while routes:
            start, end = routes[-1]
            if end >= camera_site:
                routes.pop()
            else:
                break
        answer += 1
    return answer