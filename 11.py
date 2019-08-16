class Solution:
    def intToRoman(self, num: int) -> str:
        if (num > 3999) or (num < 1):
            return False
        b = num

        s = ''
        c = ['I', 'X', 'C', 'M']
        d = ['V', 'L', 'D']
        for i in range(2,-2,-1):
            a = b // 10**(i+1)
            if a == 0:
                continue
            elif 0 < a < 4:
                s = s + a * c[i+1]
            elif a == 4:
                s = s + c[i+1] + d[i+1]
            elif 9 > a > 4:
                s = s + d[i+1] + (a%5) * c[i+1]
            else:
                s = s + c[i+1] + c[i+2]
            b = b % (10**(i+1))
        return s




solution = Solution()
a = solution.intToRoman(58)
print(a)