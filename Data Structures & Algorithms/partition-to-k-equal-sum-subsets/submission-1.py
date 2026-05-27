class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        sides = [0] * k

        length = total/k

        nums.sort()

        def dfs(i):
            # if i == len(nums) and we havent got false
            # we have necessarily dividef the shape into k pieces
            if i == len(nums):
                return True

            for side in range(k):
                if sides[side] + nums[i] <= length:
                    sides[side] += nums[i]

                    if dfs(i + 1):
                        return True

                    sides[side] -= nums[i]

                if sides[side] == 0:
                    break

            return False

        return dfs(0)

