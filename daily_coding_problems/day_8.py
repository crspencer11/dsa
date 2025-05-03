class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def universal_tree(self, root: TreeNode) -> int:
        self.count = 0

        def is_unival(node):
            if node is None:
                return True

            left_is_unival = is_unival(node.left)
            right_is_unival = is_unival(node.right)

            if not left_is_unival or not right_is_unival:
                return False

            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False

            self.count += 1
            return True

        is_unival(root)
        return self.count
