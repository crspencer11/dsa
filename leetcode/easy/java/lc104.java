class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return findDepth(root);
    }
    private int findDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftDepth = findDepth(node.left);
        int rightDepth = findDepth(node.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
