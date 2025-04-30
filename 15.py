from typing import List
# Optimal: Time: O(n^2) where n is the number of elements in the list. Space: O(m) for the result list 
# where n is the number of elements in the list and m is the number of triplets found.
# This solution uses a two-pointer approach to find the triplets that sum to zero.
# It first sorts the list and then iterates through each number.
# For each number, it uses two pointers to find the other two numbers that sum to the negative of the current number.
# This is more efficient than using a hash set to store the numbers and checking for pairs.
# This solution is optimal for large inputs as it avoids the O(n^3) time complexity of the brute force approach.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            diff = -n
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == diff:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < diff:
                    l += 1
                else:
                    r -= 1
        return res
            

        