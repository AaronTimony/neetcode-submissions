class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmp, num)
            res = max(res, curMax)

        return res