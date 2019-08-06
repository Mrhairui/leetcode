class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        y = abs(x)
        while(y != 0):
            pop = y % 10
            y = y // 10
            rev = rev * 10 + pop
            if rev > of:
                return 0
        if x > 0:
            return rev
        else:
            return -rev


solution = Solution()
a = solution.reverse(-312)
print(a)

