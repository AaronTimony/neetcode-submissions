class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0

        while l < r:
            print(l, r, people[l], people[r], boats)
            if people[l] + people[r] > limit:
                boats += 1
                r -= 1

            else:
                boats += 1
                r -= 1
                l += 1

        if l == r:
            boats += 1

        return boats