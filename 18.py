class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return None
        d = {'(': ')', '{': '}', '[': ']'}
        if s[0] not in d.keys():
            return False
        ss = []
        head = -1
        for i in range(n):
            if s[i] in d.keys():
                ss.extend(s[i])
                head = head + 1
            else:
                if head == -1 and s[i] not in d.keys():
                    return False
                if d[ss[-1]] != s[i]:
                    return False
                del ss[head]
                head = head - 1


        return True
solution = Solution()
a = solution.isValid("[])")
print(a)
