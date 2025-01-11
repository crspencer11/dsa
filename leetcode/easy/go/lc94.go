/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    traversedTree := []int{}
    traverse(root, &traversedTree)
    return traversedTree
}

func traverse(root *TreeNode, traversedTree *[]int) {
    if root == nil {
        return
    }
    traverse(root.Left, traversedTree)
    *traversedTree = append(*traversedTree, root.Val)
    traverse(root.Right, traversedTree)
}

