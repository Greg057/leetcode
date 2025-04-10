
# LeetCode 70. Climbing Stairs
# Time Complexity: O(n)
# Space Complexity: O(1) because we are using only a constant amount of space
# Approach: Use a bottom-up dynamic programming approach
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range (n - 1):
            one, two = one + two, one
        return one
    
# Math Approach
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Use the Fibonacci formula to calculate the nth Fibonacci number
# The Fibonacci numbers can be calculated using the formula:
# F(n) = (phi^n - (1 - phi)^n) / sqrt(5)
# where phi = (1 + sqrt(5)) / 2 is the golden ratio
# This formula can be used to calculate the nth Fibonacci number in O(log n) time
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)