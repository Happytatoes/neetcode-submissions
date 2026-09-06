class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []    
    
        for char in s:
            print("char is " + char)
            print(stack)
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue
            if char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0
