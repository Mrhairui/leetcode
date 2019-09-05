class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        n = len(nums)
        p = n
        while i < p:
            while nums[i] == val and i < p:
                nums.pop(i)
                p = p - 1
                if i == p:
                    return len(nums)
            i+=1
        return len(nums)


solution = Solution()
aa = solution.removeElement([0,1,2,2,3,0,4,2],2,)
print(aa)