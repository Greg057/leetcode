from typing import List

# Optimal: Time: O(n) where n is the number of words. Space: O(n)
# Bucket sort
#   1. Create a hashMap to count the frequency of each number.
#   2. Create a list of empty lists (buckets) where the index represents the frequency.
#   3. Iterate through the hashMap and append each number to the corresponding bucket.
#   4. Iterate through the buckets in reverse order and collect the numbers until we have k numbers.
#   5. Return the result list.
#   6. The time complexity is O(n) because we iterate through the list and the hashMap once.
#   7. The space complexity is O(n) because we store the frequency counts and the buckets.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for num, count in hashMap.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                