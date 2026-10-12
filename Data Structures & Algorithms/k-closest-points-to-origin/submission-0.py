from typing import List
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        def partition(left, right):
            # Randomly select a pivot
            pivot_idx = random.randint(left, right)

            # Move the pivot to the end
            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            pivot_distance = distance(points[right])
            i = left

            # Partition points by distance
            for j in range(left, right):
                if distance(points[j]) <= pivot_distance:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            # Move pivot to its final sorted position
            points[i], points[right] = points[right], points[i]

            return i

        left, right = 0, len(points) - 1
        target = k - 1

        while left <= right:
            pivot_index = partition(left, right)

            if pivot_index == target:
                break
            elif pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        return points[:k]