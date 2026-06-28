class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif char == "}":
                if not stack:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif char == ")":
                if not stack:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if not stack:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
    
        return len(stack) == 0   