# Problem: Koko Eating Bananas
# time complexity: O(n*log(max(piles))) for binary search
# space complexity: O(1) for constant space
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        l, r = 1, max(piles)
        res = r 
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m) # ceil is used to round up because Koko can only eat whole bananas. 
            if hours > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res