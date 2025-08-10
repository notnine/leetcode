#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def build() -> None:
            res = ''
            num = ''

            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    num += c
                    self.i += 1
                elif c == '[':
                    self.i += 1
                    res += int(num) * build()
                    num = ''
                elif c == ']':
                    self.i += 1
                    return res
                else:
                    res += c
                    self.i += 1
            return res    

        return build()

# @lc code=end

