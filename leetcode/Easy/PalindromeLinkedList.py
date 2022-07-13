class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head.next is not None:
            s.append(head.val)
            head = head.next
        s.append(head.val)
        return s == s[::-1]