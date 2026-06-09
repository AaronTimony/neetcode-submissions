class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        candidates.sort()

        def dfs(i, total_sum):
            if total_sum == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total_sum > target:
                return 

            subset.append(candidates[i])
            dfs(i + 1, total_sum + candidates[i])
            popped = subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total_sum)

        dfs(0, 0)
        return res