
from typing import List
import heapq
import math
# Problem: K Closest Points to Origin
# time complexity: O(k * log(n)) slightly better than O(n * log(n)) for sorting with array
# space complexity: O(n) for storing points
# The problem is to find the k closest points to the origin (0, 0) from a list of points.
# The distance from the origin is calculated using the Euclidean distance formula.
# The solution uses a min-heap to efficiently find the k closest points.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            point.insert(0, distance)
        
        heapq.heapify(points)
        
        while k > 0:
            res.append(heapq.heappop(points)[1:])
            k -= 1
        
        return res


        
