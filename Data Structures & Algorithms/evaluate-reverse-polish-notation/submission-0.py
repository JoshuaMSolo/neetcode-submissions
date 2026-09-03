class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                a = stack.pop()
                stack.append(a + stack.pop())
            elif token == "-":
                a = stack.pop()
                stack.append(stack.pop() - a)
            elif token == "*":
                a = stack.pop()
                stack.append(stack.pop() * a)
            elif token == "/":
                a = stack.pop()
                stack.append(int(stack.pop()/a))
            else :
                stack.append(int(token))
        
        return stack[0]