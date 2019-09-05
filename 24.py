class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length   # 一种边界（就是列表是最小的可能性）
        p = length
        i = 1
        while i < p:  # 一种边界就是
            while nums[i-1] == nums[i]:
                p = p - 1
                for j in range(i, p):
                    nums[j] = nums[j+1]
                nums.pop()
                if i >= p:   # 最后两个值相等这种情况
                    break
            i = i + 1
        return len(nums)


solution = Solution()
aa = solution.removeDuplicates([1,1])
print(aa)