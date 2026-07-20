class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for elem in tokens:
            if elem not in "+-*/":
                stack.append(elem)
            else:
                if elem == '+':
                    answer = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(answer))
                elif elem == '-':
                    answer = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(answer))
                elif elem == '*':
                    answer = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(answer))
                elif elem == '/':
                    if int(stack[-1]) == 0:
                        answer = 0 
                    else:
                        answer = int(int(stack[-2]) / int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(str(answer))

        return int(stack[0])