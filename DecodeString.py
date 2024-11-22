class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if (s[i] != ']'):
                stack.append(s[i])
            else:
                currStr = ""
                while stack and stack[-1] != '[':
                    currStr = stack.pop() + currStr
                stack.pop()

                value = ""
                while stack and stack[-1].isdigit():
                    value = stack.pop() + value

                stack.append(int(value) * currStr)

        return "".join(stack)

        