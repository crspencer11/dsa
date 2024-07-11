def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        else:
            temp = invertTree(root.left)
            root.left = invertTree(root.right)
            root.right = temp
        return root
