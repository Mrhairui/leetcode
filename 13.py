class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        minlength = 1000000
        if not strs:
            return ""
        for i in range(n):
            length = len(strs[i])
            if length < minlength:
                minlength = length
        minlength = int(minlength)
        res = ''
        exit_flag = False
        if minlength == 0:
            return ""
        elif n == 1:
            return strs[0]
        else:

            for i in range(minlength):
                for j in range(n - 1):
                    aa = strs[j][i]
                    bb = strs[j + 1][i]
                    if aa != bb and i == 0:
                        return ""
                    elif aa != bb:
                        exit_flag = True
                        break

                if exit_flag == True:
                    break
                res = res + aa
            return res


solution = Solution()
a = solution.longestCommonPrefix(["flower","flow","flight"])
print(a)


# 第一遍做得时候没有考虑边界条件，所以出了很多问题，你要考虑边界条件，同时按照逻辑来想，应该怎么做而不是着急上手

