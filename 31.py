class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        middle = (n - 1) // 2
        while middle != left or middle != right:
            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] >= nums[right]:
                left = middle
            middle = (right + left) // 2
            if right == left + 1 :
                if nums[left] < nums[right]:
                    middle = left
                else:
                    middle = right


