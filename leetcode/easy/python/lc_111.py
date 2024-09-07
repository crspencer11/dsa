class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            current, depth = queue.pop(0)
            if not current.left and not current.right:
                return depth
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))

