from typing import List

# Optimal: Time: O(n) where n is the number of elements in the list. Space: O(1) since res is not counted.
#   1. Create a result list initialized with 1s.
#   2. Iterate through the list from left to right, multiplying the current element with the previous product.
#   3. Iterate through the list from right to left, multiplying the current element with the next product.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre, post = 1, 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
    
# use division to calculate the product of all elements except the current element.
#   1. Calculate the product of all elements in the list.
#   2. Create a result list and fill it with the product of all elements divided by the current element.
#   3. Return the result list.
#   4. The time complexity is O(n) because we iterate through the list once to calculate the product and once to fill the result list.
#   5. The space complexity is O(1) since we only use a constant amount of space for the result list.
#   6. This approach is not optimal because it uses division, which is not allowed in this problem.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                total *= num
        
        if zero_count == 1:
            return [0 if num != 0 else total for num in nums]
        
        return [total // num for num in nums]
    
# NOT optimal Time: O(n) where n is the number of elements in the list. Space: O(n) since create prefix and postfix arrays.
#   1. Create a prefix array to store the product of all elements to the left of each element.
#   2. Create a postfix array to store the product of all elements to the right of each element.
#   3. Iterate through the list and fill the prefix and postfix arrays.
#   4. Create a result list and fill it with the product of the prefix and postfix arrays.
#   5. Return the result list.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * postfix[i]

        return res


