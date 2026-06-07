class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def _distance(x, y):
            d = (x**2 + y**2)**(1/2)
            return d

        point_d = []

        for x, y in points:
            distance = _distance(x, y)
            point_d.append([distance, x, y])

        heapq.heapify(point_d)
        res = []
        while k > 0:
            dis, x, y = heapq.heappop(point_d)
            res.append([x, y])
            k -= 1

        return res
