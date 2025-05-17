import heapq
from typing import List
# Problem: Kth Largest Element in an Array
# time complexity: O(n + k log n) for heapify and pop where n is the number of elements in the array 
#   and k is the number of elements to be popped
# space complexity: O(n) for storing the heap

# there is a better solution using quickselect with O(n) time complexity BUT O(n^2) in the worst case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
    
# alternative syntax:
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]