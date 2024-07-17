class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        vals = self.work(root)
        vals.sort()
        return vals[k-1]

    def traverse(self, root: Optional[TreeNode]):
        stack = [root]
        vals = []
        while stack:
            curr = stack.pop()
            vals.append(curr.val)
            left = curr.left
            right = curr.right
            if left and left.val < curr.val:
                stack.append(curr.left)
            if right and right.val > curr.val:
                stack.append(curr.right)
        return vals
