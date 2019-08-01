class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        longest_l = 1
        curlen = 0
        res = s[0]
        dp = [[False for _ in range(size)] for _ in range(size)]  # 存储用的表
        for r in range(1, size):
            for l in range(r):  # 暴力法也得有这个循环，完全一样。但是暴力法后面判
                # 断一个字符串是不是回文需要n的时间复杂度，动态规划不需要
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):  # 状态转移方程以及边界
                    dp[l][r] = True
                    curlen = r - l + 1   # 求得此时长度
                if curlen > longest_l: # 求得最大长度并用一个字符串记录
                    longest_l = curlen
                    res = s[l:r+1]
        return res


solution = Solution()
m = solution.longestPalindrome('fdfgabcbad')
print(m)



