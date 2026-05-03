class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for index in range(len(arr)-1, -1, -1):
            current_val = arr[index]
            arr[index] = max_val
            max_val = max(current_val, max_val)
        return arr
