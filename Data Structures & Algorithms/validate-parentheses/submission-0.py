class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {"}" : "{", "]" : "[", ")" : "("}

        stack = []

        for char in s:
            if len(stack) > 0 and char in close_brackets and stack[-1] == close_brackets[char]:
                stack.pop()

            else:
                stack.append(char)
        return stack == []