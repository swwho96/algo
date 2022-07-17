from collections import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            now = heapq.heappop(heap)
            idx = now[1]
            result.next = now[2]
            print(result)
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next