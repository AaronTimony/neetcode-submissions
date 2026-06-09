class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total_sum):
            if total_sum == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total_sum > target:
                return

            subset.append(nums[i])
            dfs(i, total_sum + nums[i])
            subset.pop()
            dfs(i + 1, total_sum)

        dfs(0, 0)
        return res

