class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = x
        b = []
        while a > 0:
            b.append(a % 10)
            a = a // 10

        n = len(b)
        c = int(n / 2)

        for i in range(c):
            if b[i] != b[n-i-1]:
                return False

        return True


solution = Solution()
print(solution.isPalindrome(121121))


# 官方解法是只反转一半的数，这样和前面一半的数比较即可