class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        final = []
        self.traverse(root, final)
        return final

    def traverse(self, root, final):
        if root is None:
            return root
        final.append(root.val)
        for child in root.children:
            self.traverse(child, final)
