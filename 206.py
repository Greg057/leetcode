from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative approach
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
# Recursive approach
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveReverse(None, head)

    def recursiveReverse(self, prev, cur):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return self.recursiveReverse(cur, next)