from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        cnt = 0
        queue = deque([root])
        while queue:
            cnt += 1
            for i in range(len(queue)):
                now = queue.popleft()
                if now.left:
                    queue.append(now.left)
                if now.right:
                    queue.append(now.right)
        return cnt