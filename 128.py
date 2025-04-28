from typing import List

# Optimal: Time: O(n) where n is the number of elements in the list. Space: O(n)
# This solution uses a set to store the numbers and checks for consecutive sequences.
# It iterates through each number and checks if it is the start of a sequence.
# If it is, it counts the length of the sequence by checking for the next numbers in the set.
# This is more efficient than sorting the list and checking for consecutive numbers.
# This solution is optimal for large inputs as it avoids the O(n log n) time complexity of sorting.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            length = 1
            if n - 1 in nums:
                continue
            i = 1
            while n + i in nums:
                length += 1
                i += 1
            longest = max(length, longest)
        return longest