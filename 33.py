class Solution:
    def searchInsert(self, nums, target) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        if nums[right] == target:
            return right
        if nums[right] < target:
            return right+1
        if nums[left] > target:
            return 0
        while left < right:
            mid = left + (right - left) // 2
            if left  == mid and nums[left] != target:
                return mid+1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

solution = Solution()
nums = [1,3,5,6]
target = 5
p =solution.searchInsert(nums, target)
print(p)

