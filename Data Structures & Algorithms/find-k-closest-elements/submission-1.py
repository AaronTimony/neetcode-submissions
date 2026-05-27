class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []

        heapq.heapify(minHeap)

        for num in arr:

            diff = -abs(num - x)
            

            if len(minHeap) < k:
                heapq.heappush(minHeap, [diff, num])
               

            elif len(minHeap) >= k and diff > minHeap[0][0]:
                
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, [diff, num])

        res = []
        for difference, number in minHeap:
            res.append(number)

        res.sort()
        return res