class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        def _reverse_nums(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
                r -= 1

        _reverse_nums(0, len(nums) - 1)
        _reverse_nums(0, k - 1)
        _reverse_nums(k, len(nums) - 1)

        

            