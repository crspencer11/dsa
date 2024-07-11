def findMode(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        d = {}
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                if curr_node.val in d:
                    d[curr_node.val] += 1
                else:
                    d[curr_node.val] = 1
                stack.append(curr_node.left)
                stack.append(curr_node.right)
        max_freq = max(d.values())
        modes = [key for key, value in d.items() if value == max_freq]

        return modes
