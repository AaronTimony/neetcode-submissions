class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1

            else:
                counts[num] += 1

            if counts[num] >= n / 2:
                return num

                