from typing import List, Optional
from binary_tree.BinaryTree import TreeNode, BinaryTree

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder and not inorder:
        return None

    node = TreeNode(preorder[0])
    rootIndexInorder = inorder.index(preorder[0])

    left_inorder = inorder[:rootIndexInorder]
    left_preorder = preorder[1: len(left_inorder) + 1]

    right_inorder = inorder[rootIndexInorder + 1:]
    right_preorder = preorder[len(left_inorder) + 1:]

    node.left = buildTree(left_preorder, left_inorder)
    node.right = buildTree(right_preorder, right_inorder)

    return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
BinaryTree.printLevelOrder(buildTree(preorder, inorder))