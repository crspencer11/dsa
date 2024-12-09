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
 *         this.right = right;t
 *     }
 * }
 */
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        layers = new ArrayList<>();
        bfs(root, 0);

        List<Double> res = new ArrayList<>();
        for (List<Integer> layer : layers) {
            double sum = 0;
            for (int val : layer) {
                sum += val;
            }
            res.add(sum / layer.size());
        }
        
        return res;
    }
    
    private List<List<Integer>> layers = new ArrayList<>();

    private void bfs(TreeNode root, int depth) {
        if (root == null) {
            return;
        }
        depth++;
        if (depth - 1 >= layers.size()) {
            layers.add(new ArrayList<>());
        }
        layers.get(depth - 1).add(root.val);
        bfs(root.left, depth);
        bfs(root.right, depth);
    }
}
