# 不要從最前面(最小)的開始放，從最大的開始放
# i → nums1 有效元素的最後一個
# j → nums2 的最後一個
# k → nums1 最後可以放答案的位置
# modify nums1 in-place

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0: # nums2 一定要全部處理完
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
