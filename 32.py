class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]   # 首先是边界条件对于这种二分查找一般是要用三个指针left right 这样至少要有两个元素
        n = len(nums)
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        while left < right and mid != left:   # 分为两步，一步是求最左边的值，一个是求最右边的值。第二个条件是为了保证2个元素的时候不陷入死循环
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else :
                right = mid  # 这个循环保证做完之后right是最左边重复的值

        if nums[left] == target:  # 这里有三种情况，一种是本省left就已经是最左边了
            left1 = left
        elif nums[right] == target:
            left1 = right
        else:
            left1 = -1
        left = 0
        right = len(nums) - 1



        while left < right:
            mid = left + (right - left) // 2
            if mid == left:
                break
            if nums[mid] <= target:
                left = mid
            else :
                right = mid
        if nums[right] == target:
            right1 = right
        elif nums[left] ==target:
            right1 = left
        else:
            right1 = -1

        if left1 != -1 and right1 == -1:
            right1 = left1
        if left1 == -1 and right1 != -1:
            left1 = right1

        return [left1, right1]

solution = Solution()
nums = [1,2,2]
target = 2
b = solution.searchRange(nums, target)
print(b)




