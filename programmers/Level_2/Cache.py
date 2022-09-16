from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    delay = 0
    cache = deque()
    for city in cities:
        # LRU 알고리즘
        if city.lower() in cache:
            delay += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            delay += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city.lower())

    return delay