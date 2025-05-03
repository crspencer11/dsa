class TreeNode {
    val: number;
    left?: TreeNode;
    right?: TreeNode;

    construcor(val = 0, left?: TreeNode, right?: TreeNode) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    universalTree(root?: TreeNode): number {
        let count = 0;

        function isUnival(node?: TreeNode): boolean {
            if (!node) return true;

            const leftUnival = isUnival(node.left);
            const rightUnival = isUnival(node.right);

            if (!leftUnival || !rightUnival) return false;

            if (node.left && node.left.val !== node.val) return false;
            if (node.right && node.right.val !== node.val) return false;

            count++;
            return true;
        }

        isUnival(root)
        return count;
    }
}
