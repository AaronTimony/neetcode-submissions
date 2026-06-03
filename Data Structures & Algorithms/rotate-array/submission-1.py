class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if len(nums) == 0:
            return []


        while k > 0:
            last = nums[len(nums) - 1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last

            k -= 1

            