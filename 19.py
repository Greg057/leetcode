# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# one Pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    

# two Pass
# time complexity: O(n)
# space complexity: O(1) for constant space
# The algorithm uses O(n) time to find the length of the list and then O(n) time to remove the nth node from the end.
# However, since we are not using any extra space (except for a few pointers), the space complexity is O(1).
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        slow = head
        length = 0
        while slow:
            length += 1
            slow = slow.next
        
        temp = head
        while length - n - 1 > 0:
            temp = temp.next
            length -= 1

        temp.next = temp.next.next
        return head.next
    