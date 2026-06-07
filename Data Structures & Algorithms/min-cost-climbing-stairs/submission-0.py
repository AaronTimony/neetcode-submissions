class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion relation messed up, base case messed up
        memo = {len(cost): 0, len(cost) + 1 : 0}
        if len(cost) == 0:
            return 0

        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost[0], cost[1])

        def dfs(i):

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        return min(dfs(0), dfs(1))