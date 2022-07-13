class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        while now and now.next:
            now.val, now.next.val = now.next.val, now.val
            now = now.next.next
        return head