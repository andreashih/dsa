# 找最小可行速度

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 # 最小速度是每小時 1 根
        right = max(piles) # 最大速度是每小時 max(piles) 根

        while left < right:
            speed = (left + right) // 2 # 從中間挑一個速度來測試

            # hours_needed = sum(
            #     (pile + speed - 1) // speed
            #     for pile in piles
            # )

            hours_needed = 0
            for pile in piles:
                hours_for_this_pile = pile // speed

                if pile % speed != 0:
                    hours_for_this_pile += 1
                
                hours_needed += hours_for_this_pile
            
            if hours_needed <= h:
                # 目前速度 (speed) 可行，把最大速度 (right) 換成 speed，繼續找更慢的速度
                right = speed
            else:
                # 目前速度太慢，把最小速度 (left) 換成 speed，繼續提高速度
                left = speed + 1

        return left
        