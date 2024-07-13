class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        results = []
        while queue:
            level = len(queue)
            for i in range(level):
                curr_node = queue.popleft()
                if i == level - 1:
                    results.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return results
