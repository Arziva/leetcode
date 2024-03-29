
from collections import deque


class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for rd, cd in directions:
                    r, c = rd+row, cd + col

                    if( (r) in range(rows) and
                        (c) in range(cols) and
                        grid[r][c] == "1" and 
                        (r,c) not in visit
                    ):
                        q.append((r,c))
                        visit.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands