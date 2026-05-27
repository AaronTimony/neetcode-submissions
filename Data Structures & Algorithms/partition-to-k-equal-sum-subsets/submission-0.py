class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        # if its divisible by 4 and we can 


        sides = [0] * k

        length = total/k

        nums.sort(reverse=True)

        def dfs(i):
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