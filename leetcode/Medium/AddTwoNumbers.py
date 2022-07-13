class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        two_num_sum, prev = [0,0], None
        idx = 0
        while l1 or l2:
            if l1:
                two_num_sum[0] += (l1.val) * (10**idx)
                l1 = l1.next
            if l2:
                two_num_sum[1] += (l2.val) * (10**idx)
                l2 = l2.next
            idx += 1
        for i in str(sum(two_num_sum)):
            node = ListNode(i)
            node.next = prev
            prev = node
        return node