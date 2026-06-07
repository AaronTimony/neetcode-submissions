class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {len(nums): 0, len(nums)+ 1: 0, len(nums) + 2: 0}

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))


            return memo[i]
            

        return max(dfs(0), dfs(1))