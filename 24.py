class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length
        p = length
        i = 1
        while i < p:
            while nums[i-1] == nums[i]:
                p = p - 1
                for j in range(i, p):
                    nums[j] = nums[j+1]
                nums.pop()
                if i >= p:
                    break
            i = i + 1
        return len(nums)


solution = Solution()
aa = solution.removeDuplicates([1,1])
print(aa)