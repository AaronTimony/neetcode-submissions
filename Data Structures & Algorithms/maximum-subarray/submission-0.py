class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxi = nums[0]

        for num in nums:
            if curSum < 0:
                curSum = 0

            curSum += num
            maxi = max(maxi, curSum)


        return maxi