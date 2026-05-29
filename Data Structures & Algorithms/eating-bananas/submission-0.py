class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r


        while l <= r:
            m = l + (r - l) // 2
            t = 0

            for pile in piles:
                t += math.ceil(pile/m)

            if t > h:
                l = m + 1


            elif t <= h:
                min_k = m

                r = m - 1

        return min_k


