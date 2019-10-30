from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        while left < n:
            if height[left] > height[left+1]:
                break
        right = left + 1

        while right < n:
            if middle < left and middle < right:
                if left <= right:
                    water = left - middle