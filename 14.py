class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return None
        maxlist = max(nums)
        minlist = min(nums)
        if maxlist == 0 and minlist ==0:
            return [[0,0,0],]
        nums = sorted(nums)
        cc = []
        for i in range(n-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            else:
                for j in range(i+1,n-1):

                    if nums[j] == nums[j - 1] and j > i+1:
                        continue
                    else:
                        res = 0 - nums[i] - nums[j]
                        for t in range(j+1, n):

                            if nums[t] == nums[t - 1] and t > j + 1:
                                continue
                            else:
                                if nums[t] == res:
                                    cc.append([nums[i], nums[j], nums[t]])
        return cc


solution = Solution()
aa = solution.threeSum([-1,0,1,2,-1,-4])
print(aa)


