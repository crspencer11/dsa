class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> results = new ArrayList<>();
        traverse(root, results);
        return results;
    }
    private void traverse(TreeNode root, List<Integer> results) {
        if (root == null) {
            return;
        }
        results.add(root.val);
        traverse(root.left, results);
        traverse(root.right, results);
    }
}
