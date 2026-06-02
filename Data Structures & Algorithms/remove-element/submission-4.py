class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # first k elements are != val
        # So we are going to find val, switch that index with len - k update k

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1

            else:
                i += 1
            
        return n