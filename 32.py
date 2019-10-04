class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        n = len(nums)
        left = 0
        right = len(nums) - 1
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        if n == 2:
            if nums[0] == target and nums[1] == target:
                return [0, 1]
            elif nums[0] == target and nums[1] != target:
                return [0, 0]
            elif nums[0] != target and nums[1] == target:
                return [1, 1]
            elif nums[0] != target and nums[1] != target:
                return [-1, -1]


        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else :
                right = mid
        if nums[right] == target:
            left1 = right
        else:
            left1 = -1
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else :
                right = mid
        if nums[left] == target:
            right1 = left
        else:
            right1 = -1

        if left1 != -1 and right1 == -1:
            right1 = left1
        if left1 == -1 and right1 != -1:
            left1 = right1

        return [left1, right1]

solution = Solution()
nums = [1,2,3]
target = 1
b = solution.searchRange(nums, target)
print(b)




