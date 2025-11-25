from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    @staticmethod
    def create(arr):
        """Create a binary tree from an array (like LeetCode input)"""
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            current = queue.popleft()

            # Left child
            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1

        return root

    @staticmethod
    def printLevelOrder(root):
        """Print the tree in level order (like LeetCode)"""
        if root is None:
            print("[]")
            return

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if node is None:
                result.append("null")
                continue

            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        # remove trailing nulls
        while result and result[-1] == "null":
            result.pop()

        print(result)

    @staticmethod
    def printInorder(root):
        """Iterative inorder traversal"""
        if root is None:
            print("[]")
            return

        stack = []
        curr = root

        print("[", end="")

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(str(curr.val) + ",", end="")
            curr = curr.right

        print("]")
