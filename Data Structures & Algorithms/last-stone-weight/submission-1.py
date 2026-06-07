class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y < x:
                heapq.heappush(stones, y - x)

            elif y == x:
                continue

            else:
                print("Invalid Heap")

            
        return -stones[0] if stones else 0