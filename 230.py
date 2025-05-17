class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# kth smallest element in a binary search tree
# time complexity: O(n)
# space complexity: O(n) for the array
# The algorithm uses O(n) time to traverse the tree and O(n) space to store the elements in the array.
# The space complexity is O(n) because in the worst case, we need to store all the elements in the array.
# The algorithm uses a depth-first search (DFS) approach to traverse the tree in an in-order manner,
# which means we visit the left subtree, then the current node, and finally the right subtree.
# This ensures that the elements are stored in sorted order in the array.      
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(root):
            if not root: return None
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        return arr[k - 1]