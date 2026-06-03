class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        res = []

        nums.sort()

        a = 0

        while a < len(nums) - 3:

            b = a + 1

            while b < len(nums) - 2:
                l = b + 1
                r = len(nums) - 1

                while l < r:
                    total = nums[a] + nums[b] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[a], nums[b], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif total < target:
                        l += 1

                    elif total > target:
                        r -= 1
                
                b += 1
                while b < len(nums) - 2 and nums[b] == nums[b - 1]:
                    b += 1
            a += 1
            while a < len(nums) - 3 and nums[a] == nums[a - 1]:
                a += 1

        return res

                