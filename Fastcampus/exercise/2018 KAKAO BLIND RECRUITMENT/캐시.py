def is_in_cache(cache, city):
    for idx in range(len(cache)):
        if cache[idx][1] == city:
            return idx
    else:
        return -1


def solution(cacheSize, cities):
    cache = []
    time = 0
    if not cacheSize:
        return len(cities)*5
    # cities 하나하나 본다
    for city in cities:
        result = is_in_cache(cache, city.lower())
        # 캐시에 있다면
        if result != -1:
            time += 1  # hit
            # 최근 사용 업데이트
            for c in cache:
                c[0] += 1
            cache[result][0] = 0
        # 캐시에 없다면
        else:
            time += 5  # miss
            # 캐시가 비었다면
            if len(cache) < cacheSize:
                for c in cache:
                    c[0] += 1
                # 추가해주기
                cache.append([0, city.lower()])
            # 캐시가 꽉 차있다면 LRU 삭제하고 추가해주기
            else:
                cache.sort(key=lambda x: x[0])
                cache.pop()
                for c in cache:
                    c[0] += 1
                cache.append([0, city.lower()])
    answer = time
    return time


print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
