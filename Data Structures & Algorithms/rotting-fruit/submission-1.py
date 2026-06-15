class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Definitely BFS 
        q = deque()
        COLS = len(grid[0])
        ROWS = len(grid)
        visit = set()

        def rotBanana(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return

            grid[r][c] = 2

            q.append([r, c])
            visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))

        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                rotBanana(r + 1, c)
                rotBanana(r - 1, c)
                rotBanana(r, c + 1)
                rotBanana(r, c - 1)

            minutes += 1

        print(grid)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes - 1 if minutes > 0 else 0
                
                