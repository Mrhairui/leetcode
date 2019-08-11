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

# 这个虽然简单，但是很有代表性，代表着栈这种数据结构，前后交换很明显就可以用栈
# 栈的实现：通过把数赋给pop然后一直更新pop（代表栈顶）。但是没有压栈的过程也就是没有存储栈，因为特殊所以可以直接用每次乘以10来代表