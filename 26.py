class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if (needle or haystack) == '' or  (needle == ''):
            return 0
        if haystack == '':
            return -1
        for i in range(n-m):
            for j in range(0, m):
                if haystack[j+i] != needle[j] and i==n-m-1:
                    return -1
                if haystack[j+i] != needle[j]:
                    break
                if j == m-1:
                    return i




solution = Solution()
aa = solution.strStr(haystack = "", needle = "a")
print(aa)