# 到第 5 階的方法數 = 到第 4 階的方法數 + 到第 3 階的方法數
# ways(5) = ways(4) + ways(3)
# ways(n) = ways(n - 1) + ways(n - 2)
# ways(1) = 1, ways(2) = 2
# Fibonacci-like sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n

        # Number of ways to reach step 1 and 2
        ways_1 = 1 # 前一階的答案
        ways_2 = 2 # 前兩階的答案

        # Calculate the number of ways for each step from 3 to n
        # 要算下一階有幾種走法，只要看前面兩階的答案
        for step in range(3, n + 1):
            current = ways_1 + ways_2

            # Shift the values for the next iteration
            ways_1 = ways_2
            ways_2 = current
        
        return ways_2

        
        