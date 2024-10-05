/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    int diameter;

    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        findDiameter(root);
        return diameter;
    }

    private int findDiameter(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = findDiameter(root.left);
        int right = findDiameter(root.right);
        diameter = Math.max(diameter, left + right);
        return Math.max(left, right) + 1;
    }
}

