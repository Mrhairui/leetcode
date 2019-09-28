class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0 # 记住这个很重要是判断你的数据集是不是空集如果是的话，没必要往下，同时往下可能会出错
        stack = []  # 利用数组可以完全实现栈的功能
        res = [] # 记录栈弹出的内容，也可以用数组
        for i in range(len(s)):
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
            if s[i] == '(':
                stack.append(i)
        res.sort()

        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n-1 and res[j+1] == res[j] + 1:
                j +=1
            ans = max(ans, j-i+1)
            i = j + 1
        return ans

