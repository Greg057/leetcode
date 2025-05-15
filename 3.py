# Given a string s, find the length of the longest substring without repeating characters.
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res