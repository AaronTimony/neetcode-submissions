class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1:
            return nums[0]

        
        

        def dfs(i, first_robbed):
            if i == n - 1:
                return 0 if first_robbed else nums[n - 1]

            if i >= n:
                return 0

            if (i, first_robbed) in memo:
                return memo[(i, first_robbed)]

            memo[(i, first_robbed)] = max(dfs(i + 1, first_robbed), nums[i] + dfs(i + 2, first_robbed))
            print(i, nums[i], memo)
            return memo[(i, first_robbed)]


        return max(dfs(0, True), dfs(1, False))


            