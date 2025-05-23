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
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) {
            return root2;
        } 
        else if (root2 == null) {
            return root1;
        } 
        else {
            TreeNode merged_tree = new TreeNode(root1.val + root2.val);
            merged_tree.left = mergeTrees(root1.left, root2.left);
            merged_tree.right = mergeTrees(root1.right, root2.right);
            return merged_tree;
        }
    }
}

