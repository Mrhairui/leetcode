# 讲的是如何使用队列，队列是用一个集合来表示，制定一个指针用来指定队列的头部

class Solution():
    def length_of_string(self, string):
        n = len(string)  # 求字符串的长度
        ss = set() # 队列可以用集合来定义
        left = 0
        maxcount = 0
        count = 0
        for i in range(n):
            count += 1
            while string[i] in ss: # 我刚开始想的是用if是不行的，你需要不停的循环直到左边相同的取消完了
                ss.remove(string[left])  # remove是移除，add是增加
                left += 1
                count -= 1
            if count > maxcount:     # 记录最大的个数
                maxcount = count
            ss.add(string[i])  # 字符串可以利用下表来索引,add 往集合里面添加元素
        return maxcount


string = "abcabcbb"
solution = Solution()
maxcount = solution.length_of_string(string)
print(maxcount)

