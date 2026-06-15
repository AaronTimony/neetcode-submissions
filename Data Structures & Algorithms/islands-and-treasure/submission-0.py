class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs in 4 dirn and if land return min distance to 0

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return 
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)

            dist += 1
