def countNodes(root):
    if not root:
        return 0
    left_depth = get_left_depth(root)
    right_depth = get_right_depth(root)
    if left_depth == right_depth:
        2 ** left_depth - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

def get_left_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.left
    return depth

def get_right_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.right
    return depth

