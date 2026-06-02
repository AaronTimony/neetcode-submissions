class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                output = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(output))

            elif token == "-":
                output = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(output))

            elif token == "*":
                output = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(output))                

            elif token == "/":
                output = float(stack[-2]) / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(output))

            else:
                stack.append(int(token))

        return stack[0]


