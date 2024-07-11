def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            tree = TreeNode(nums[mid])
            tree.left = self.sortedArrayToBST(nums[:mid])
            tree.right = self.sortedArrayToBST(nums[mid+1:])
            return tree
