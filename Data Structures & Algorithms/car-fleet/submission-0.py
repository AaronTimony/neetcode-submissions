class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If a car in position behind, catches a car ahead, it stops being in fleet.
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for pos, spd in pair:
            t = (target - pos)/spd
            stack.append(t)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)