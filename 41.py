class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        ps = len(p)
        i = 0
        j = 0
        pp = 0
        aa = True
        while pp < ps:
            if p[pp] != '*':
                aa = False
                break
            pp = pp + 1



        if ns == 0 and ps == 0:
            return True
        elif ns == 0 and ps == 1 and p[0] == '?':
            return True
        elif ns == 0 and aa:
            return True
        elif ns == 0 and not aa:
            return False
        elif ns != 0 and ps == 0:
            return False

        while i < ns or j < ps:
            if p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                if ps == 1 or j == ps-1:
                    return True
                if p[j + 1] == s[i]:
                    i += 1
                    j += 2
                else:
                    i += 1
            elif p[j] != '?' and p[j] != '*' and s[i] == p[j]:
                i += 1
                j += 1
            else:
                return False
            if i == ns and j == ps or j == ps + 1:
                return True
            if i == ns and j != ps:
                return False
            if i != ns and j == ps:
                return False




if __name__ == '__main__':
    s = "abefcdgiescdfimde"

    p = "ab*cd?i*de"
    solution = Solution()
    result = solution.isMatch(s, p)
    print(result)
