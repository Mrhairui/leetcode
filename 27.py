class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        divd= dividend
        dior = divisor
        res = 0
        sign = 1 if divd ^ dior >= 0 else -1  # 这是一种判断两个符号是否相同的方法
        # print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)   # 一个数是否在范围内

solution = Solution()
aa = solution.divide(1,1)
print(aa)