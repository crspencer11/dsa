class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> results = new ArrayList<>();
        traverse(root, results);
        return results;
    }

    private void traverse(TreeNode root, List<Integer> results) {
        if (root == null) {
            return;
        }
        traverse(root.left, results);
        results.add(root.val);
        traverse(root.right, results);
    }
}

