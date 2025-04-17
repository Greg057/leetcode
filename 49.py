from typing import List

# NOT OPTIMAL: Time: O(n * k log k) sinc sorted(word) takes O(k log k). Space: O(n * k)
# where n is the number of words and k is max length word.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            wordSorted = ''.join(sorted(word))
            if wordSorted not in res:
                res[wordSorted] = []
            res[wordSorted].append(word)
        return res.values()
    

# Optimal: Time: O(n * k) where n is the number of words and k is max length word. Space: O(n * k)
# defaultdict(list) means:
#   "If a key doesn't exist, automatically set its value to an empty list ([]) before doing anything else."
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[tuple(count)].append(word)
        return res.values()
    
# ALSO OPTIMAL using defaultdict
# defaultdict(list) means:
#   "If a key doesn't exist, automatically set its value to an empty list ([]) before doing anything else."
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(word)
        return res.values()