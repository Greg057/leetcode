from typing import List

# easier than using stack:
# time complexity: O(nlogn) for sorting
# space complexity: O(n) for storing pairs
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs.sort(reverse=True)
        fleet = 0
        time = 0

        for position, speed in pairs:
            destination_time = (target - position)/speed
            if destination_time > time:
                time = destination_time
                fleet += 1
        return fleet 