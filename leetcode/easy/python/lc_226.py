def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        else:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp
        return root
