# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid # 猜中
            elif result == -1:
                # mid 太大，往較小數字找
                right = mid - 1
            else:
                # mid 太小，往較大數字找
                left = mid + 1