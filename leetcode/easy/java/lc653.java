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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> resultList = new ArrayList<>();
        inorderTraversal(root, resultList);
        
        int left = 0;
        int right = resultList.size() - 1;
        while (left < right) {
            int currSum = resultList.get(left) + resultList.get(right);
            if (currSum < k) {
                left++;
            } else if (currSum > k) {
                right--;
            } else {
                return true;
            }
        }
        return false;
    }

    private void inorderTraversal(TreeNode rootNode, List<Integer> traversalRes) {
        if (rootNode == null) {
            return;
        }
        inorderTraversal(rootNode.left, traversalRes);
        traversalRes.add(rootNode.val);
        inorderTraversal(rootNode.right, traversalRes);
    }
}

