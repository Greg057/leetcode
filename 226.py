# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# time complexity: O(n)
# space complexity: O(n) because worst case scenario where every node has only the left child 
#   (the right child is null), it is essentially a linked list, so have to make n recursive 
#   calls and store n stack frames, where n is the number of nodes
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root