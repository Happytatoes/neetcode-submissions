class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        n = len(s)
        l = list(s)

        for i in range(0, n):
            elem = s[i]
            
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)
            if elem == ')' or elem == ']' or elem == '}':
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == '(' and elem == ')':
                        stack.pop()
                    elif stack[-1] == '[' and elem == ']':
                        stack.pop()
                    elif stack[-1] == '{' and elem == '}':
                        stack.pop()
                    else: 
                        return False
            
        if len(stack) == 0:
            return True
        return False
                        