class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(balance_left):
            if balance_left == 0:
                return 0

            if balance_left in memo:
                return memo[balance_left]

            res = 1e9
            for coin in coins:
                if coin <= balance_left:
                    res = min(res, 1 + dfs(balance_left - coin))

            memo[balance_left] = res

            return res

        minCoins = dfs(amount)

        return -1 if minCoins >= 1e9 else minCoins
        




                
                
        