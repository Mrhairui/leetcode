from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        i = 0
        p = res
        nums.sort()
        while i < n:
            if nums[i] == p:
                p  =  p + 1
            i+=1
        return p

if __name__ == '__main__':
    candidates = [3,4,-1,1]
    target = 8
    solution = Solution()
    result = solution.firstMissingPositive(candidates)
    print(result)


