# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  
        final = []
        queue = [root]
        while queue:
            level = []
            next_node = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            final.append(level)
            queue = next_node
        return final
