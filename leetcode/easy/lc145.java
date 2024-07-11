class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> results = new ArrayList<>();
        traverse(root, results);
        return results;
    }
    private void traverse(TreeNode root, List<Integer> results) {
        if (root == null) {
            return;
        }
        traverse(root.left, results);
        traverse(root.right, results);
        results.add(root.val);
    }
}
