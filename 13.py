class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        minlength = float('inf')
        for i in range(n):
            length = len(strs[i])
            if length < minlength:
                minlength = length
        dd = 0
        dd = int(minlength)

        for i in range(dd):
            for j in range(n - 1):
                aa = strs[j][i]
                bb = strs[j + 1][i]
                if aa != bb:
                    return strs[0][0:i]


solution = Solution()
a = solution.longestCommonPrefix(["dag","dacecar","dar"])
print(a)




