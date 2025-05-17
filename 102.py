# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
import collections

# BFS
# level order traversal of a binary tree
# time complexity: O(n)
# space complexity: O(n) for the queue
# The algorithm uses O(n) time to traverse the tree and O(n) space to store the nodes in the queue.
# The space complexity is O(n) because in the worst case, the queue can store all the nodes at the last level of the tree.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLength = len(q)
            level = []
            for i in range(qLength):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
