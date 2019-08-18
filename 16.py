class Solution:
    def letterCombinations(self, digits):
        n = len(digits)
        if n < 1:
            return None   # 这一句一定要加上这是边界条件，如果不加后面字符串就会越界
        d2 = {'2':['a', 'b', 'c']}
        d3 = {'3': ['d', 'e', 'f']}
        d4 = {'4': ['g', 'h', 'i']}
        d5 = {'5': ['j', 'k', 'l']}
        d6 = {'6': ['m', 'n', 'o']}
        d7 = {'7': ['p', 'q', 'r', 's']}
        d8 = {'8': ['t', 'u', 'v']}
        d9 = {'9': ['w', 'x', 'y', 'z']}
        dd = [d2, d3, d4, d5, d6, d7, d8, d9]
        a = int(digits[0])
        ex = dd[a - 2][digits[0]]
        for i in range(1,n):
            p = int(digits[i])
            if p == 7 or p == 9:
                ex = [pp+dd[p-2][digits[i]][0] for pp in ex] + [pp+dd[p-2][digits[i]][1] for pp in ex] + [pp+dd[p-2][digits[i]][2] for pp in ex] + [pp+dd[p-2][digits[i]][3] for pp in ex]
            else:
                ex = [pp + dd[p - 2][digits[i]][0] for pp in ex] + [pp + dd[p - 2][digits[i]][1] for pp in ex] + [
                    pp + dd[p - 2][digits[i]][2] for pp in ex]

        return ex

solution = Solution()
aa = solution.letterCombinations("27")
print(aa)



