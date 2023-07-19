def solve():
    n = int(input())
    k = int(input())
    s, e = 1, k
    result = 0
    while s <= e:
        mid = (s+e) // 2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)
        if cnt < k:
            s = mid+1
        else:
            result = mid
            e = mid-1
    print(result)
solve()

# ----------------------------------------------------------------------

def solve():
    # 입력 받기
    N = int(input())
    k = int(input())
    
    # 이진 탐색을 위한 범위 설정
    lo, hi = 0, k

    # 이진 탐색 시작
    while lo < hi:
        mid = (lo + hi) // 2   # 중간값 계산
        
        # mid보다 작거나 같은 수의 개수 세기
        count = 0
        for i in range(1, N+1):
            temp = mid // i  # i번째 행에서 mid보다 작거나 같은 수의 개수
            if temp > N:    # 하지만 이 개수는 N을 초과할 수 없음
                temp = N
            count += temp   # 전체 개수에 더하기
        
        # count와 k 비교하여 탐색 범위 업데이트
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    
    # k번째 수 출력
    print(lo)

solve()