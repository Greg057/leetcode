# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# validate binary search tree
# time complexity: O(n)
# Space: O(N) This is because the DFS function is recursively called for each node in the BST, 
#   potentially leading to a call stack depth proportional to the number of nodes
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minVal, maxVal):
            if not root: return True
            if not minVal < root.val < maxVal:
                return False
            return dfs(root.left, minVal, root.val) and dfs(root.right, root.val, maxVal)
            
        return dfs(root, float("-inf"), float("inf"))
            