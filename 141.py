# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


# A set is used instead of a list or dict because it provides O(1) 
#   average time complexity for membership checks and avoids duplicates

# NOT OPTIMAL SOLUTION
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

# BETTER SOLUTION
# Time Complexity: O(n)
# Space Complexity: O(1)
# Floyd's Tortoise and Hare algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        