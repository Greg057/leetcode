# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# Time Complexity: O(n)
# Space Complexity: O(n)
# Code explanation:
# - We are using a depth-first search (DFS) approach to traverse the binary tree.
# - The function `dfs` calculates the height of the left and right subtrees of each node.
# - The diameter of the binary tree is the maximum value of `left + right` for all nodes
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res

