
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            root.left, root.right = Solution().invertTree(root.right), Solution().invertTree(root.left)
        return root