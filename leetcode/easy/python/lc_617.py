def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root1, root2)
        
    def traverse(self, node1, node2):
        if node1 and node2:
            root = TreeNode(node1.val + node2.val)
            root.left = self.traverse(node1.left, node2.left)
            root.right = self.traverse(node1.right, node2.right)
            return root
        return node1 or node2
