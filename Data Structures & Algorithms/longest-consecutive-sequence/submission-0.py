class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            sequence = 1
            base_num = num
            while base_num + 1 in nums:
                sequence += 1
                base_num += 1

            res = max(res, sequence)

        return res
            