import heapq
from typing import List

# Use a max heap to store the stones
# The root of the max heap will be the largest stone
# O(n) for heapify
# getting the max item fron Heap is O(log n)
# so Time Complexity: O(n log n)
# Space Complexity: O(n) for storing the stones in the heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)  

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones) 
            stone2 = -heapq.heappop(stones)
            if stone1 > stone2:
                heapq.heappush(stones, - (stone1 - stone2))

        return -stones[0] if stones else 0 