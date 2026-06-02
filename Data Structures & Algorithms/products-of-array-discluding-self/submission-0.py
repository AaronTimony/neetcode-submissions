class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        temp = [1] * len(nums)

        # take all left side, then all right side or vice versa actually
        # Remove index i, have a temp array multiply by all left side, then right side

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp[i] *= nums[j]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                temp[i] *= nums[j]

        return temp



