# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# recursive solution is a possibility of a stack overflow. In this exact problem this is not an 
# issue because it's mentioned there could be maximum 100 elements in a tree.
# Ask Interviewer for a maximum possible number of elements in a data structure and you implement a
# recursive solution in an interview, you can expect to lose some points
# use iterative solution instead in this case
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
            
        if not q or not p or q.val != p.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# iterative solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
                
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True