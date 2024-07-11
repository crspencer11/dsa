class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }
        else {
            int total = 0;
            if (root.left != null && root.left.left == null) {
                if (root.left.left == null) {
                    if (root.left.right == null) {
                        total += root.left.val;
                    }
                }
            }
            total += sumOfLeftLeaves(root.left);
            total += sumOfLeftLeaves(root.right);
            return total;
        }
    }
}
