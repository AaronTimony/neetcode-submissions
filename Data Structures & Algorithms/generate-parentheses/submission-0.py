class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        count = {"(": 0, ")": 0}

        def dfs():
            if count["("] == n and count[")"] == n:
                res.append("".join(stack))
                return

            if count["("] < n:
                stack.append("(")
                count["("] += 1
                dfs()
                stack.pop()
                count["("] -= 1

            if count[")"] < count["("]:
                stack.append(")")
                count[")"] += 1
                dfs()
                stack.pop()
                count[")"] -= 1

        dfs()
        return res

 

            