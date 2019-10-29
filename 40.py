from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        middle = 1
        right = 2
        n = len(height)
        while right < n:
            if middle < left and middle < right:
                if left <= right:
                    water = left - middle