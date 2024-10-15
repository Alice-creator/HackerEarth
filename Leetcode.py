class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = list()
        for i in s:
            check = False
            if i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True

# temp = Solution()
# print(temp.isValid(s = '()'))
