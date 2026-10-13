from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        # 第一輪：計算每種顏色出現幾次
        for num in nums:
            counts[num] += 1

        # 第二輪：依照桶子的數量寫回 nums
        index = 0

        for color in range(3):
            for _ in range(counts[color]):
                nums[index] = color
                index += 1
        