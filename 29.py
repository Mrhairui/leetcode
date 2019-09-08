class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        firstindex = -1
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstindex = i
                break
        if firstindex == -1:
            reverse(nums, 0, n-1)
            return nums
        secondindex = -1
        for i in range(n-1, firstindex, -1):
            if nums[i] > nums[firstindex]:
                secondindex = i
                break
        nums[firstindex], nums[secondindex] = nums[secondindex], nums[firstindex]
        reverse(nums, firstindex+1, n-1)
        return nums

solution = Solution()
aa = solution.nextPermutation([3,2,1])
print(aa)






