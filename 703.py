import heapq
from typing import List

# Kth Largest Element in a Stream
# Time Complexity: O(m * log k) for each add operation where m number of calls to add 
# Space Complexity: O(k) for storing the k largest elements in the min heap
# Approach: Use a min heap to store the k largest elements
# The root of the min heap will be the kth largest element
# If the size of the heap exceeds k, remove the smallest element
# This ensures that we always have the k largest elements in the heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]