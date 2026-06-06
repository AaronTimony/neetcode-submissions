class Solution:
    def climbStairs(self, n: int) -> int:
        
        steps = [0] * n
        if n == 0:
            return 1

        if n == 1:
            return 1

        steps[0] = 1
        steps[1] = 2

        for i in range(2, len(steps)):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[-1]