# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# time complexity: O(n)
# space complexity: O(1) for constant space
# The algorithm uses O(n) time to find the middle of the list and reverse the second half of the list.
# Then it uses O(n) time to merge the two halves together. However, since we are not using any extra space
# (except for a few pointers), the space complexity is O(1).
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2     