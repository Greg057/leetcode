# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# DFS - Recursive solution
# Time Complexity: O(n)
# Space Complexity: O(n) because worst case scenario where every node has only the left child
#   (the right child is null), it is essentially a linked list, so have to make n recursive
#   calls and store n stack frames, where n is the number of nodes
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# BFS - Using deque
# Time Complexity: O(n)
# Space Complexity: O(n) because we need to store the nodes in the queue
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
    
# DFS - Iterative solution
# Time Complexity: O(n)
# Space Complexity: O(n) because we need to store the nodes in the stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth
