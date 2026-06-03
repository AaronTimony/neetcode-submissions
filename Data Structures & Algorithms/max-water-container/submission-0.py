class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        # The right side is limiting factor

        while l < r:
            bottom = r - l
            
            h = min(heights[l], heights[r])

            area = bottom * h

            res = max(res, bottom * h)

            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1

        return res

