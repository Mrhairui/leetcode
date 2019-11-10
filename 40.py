from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        if n == 0 or n == 1 or n==2:
            return 0
        res = 0
        right = n-1
        while left < n-1:
            if height[left] > height[left+1]:
                break
            left += 1
        if left == n-1:
            return 0
        while right >= 0:
            if height[right] > height[right-1]:
                break
            right -= 1
            if right ==1:
                return 0
        p = height[left-1:right + 1]

        index = height.index(max(height))
        pp = left
        while left < index:
            pp = pp + 1
            if height[pp] >= height[left]:
                left = pp
            res = res + (height[left] - height[pp])
        pp = right
        while right > index:
            pp = pp - 1
            if height[pp] >= height[right]:
                right = pp
            res = res + (height[right] - height[pp])

        return res




if __name__ == '__main__':
    height = [1,7,8]
    solution = Solution()
    result = solution.trap(height)
    print(result)


