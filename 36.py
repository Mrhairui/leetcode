class Solution:
    def countAndSay(self, n: int) -> str:
        def next_num(tmp):
            res = ''
            i = 0
            tmp_n = len(tmp)
            while i < tmp_n:
                count = 1
                while i < tmp_n - 1 and tmp[i] == tmp[i+1]:
                    count += 1
                    i += 1
                res += (str(count) + tmp[i])
                i += 1
            return res
        res = '1'
        for i in range(1, n):
            res = next_num(res)
        return res

            