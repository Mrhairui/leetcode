class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or # 如果首位不匹配但是第二位是*，则需要匹配后面的字符
                    first_match and self.isMatch(text[1:], pattern)) # 如果首位匹配，第二位是*，则说明text第二位必须是pattern[0]，也就是这样匹配
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])  # 如果第一位匹配第二位正常匹配



