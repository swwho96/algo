import heapq
from collections import deque
List = list

class Solution:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        deq, ans = deque(), []

        for i in range(len(nums)):
            # 앞에서부터 out of window -> 제거
            if deq and i-deq[0] == k:
                deq.popleft()

            # 뒤에서부터 현재 추가할 숫자보다 작으면 -> 제거 (deq에 불필요한 숫자 없도록!)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            deq.append(i) # 현재 숫자 추가( (i, num[i])로 저장해도 되나, 숫자 위치 저장만 해 space 줄임)
            # 출력 부분 (현재 위치 >= window size일 때)
            if i+1 >= k:
                ans.append(nums[deq[0]])  # 맨 앞은 현재 window 에서 가장 큰 수
            print(deq, ans)

        return ans

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    heap = list()
    output = list()
    
    for i in range(0, len(nums)):
        while len(heap) and i-k >= heap[0][1]:
            heapq.heappop(heap)
        heapq.heappush(heap, (-nums[i], i))
        if len(heap) >= k:
            output.append(-1 * heap[0][0])
        print(i,k,heap,output)
    
    return output

print(Solution.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))