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
            for l in range(r):
                if s[l] == s[r] and (r-1 <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    curlen = r - l + 1
                if curlen > longest_l:
                    longest_l = curlen
                    res = s[l:r+1]
        return res

solution = Solution()
m = solution.longestPalindrome('abcbd')
print(m)



