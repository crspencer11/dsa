/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode) {
    if root == nil {
        return
    }
    head := root
    for head != nil {
        if head.Left != nil {
            prev := head.Left
            for prev.Right != nil {
                prev = prev.Right
            }
            prev.Right = head.Right
            head.Right = head.Left
            head.Left = nil
        }
        head = head.Right
    }
}

