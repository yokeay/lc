class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                # 若栈空，却遇到右括号
                if not stack:
                    return False
                
                top = stack[-1]
                if (char == ')' and top == '(') or \
                   (char == '}' and top == '{') or \
                   (char == ']' and top == '['):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0



if __name__ == '__main__':
    s = Solution()
    str = "()[]{}"
    print(s.isValid(str))