class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       row = len(grid)
       col = len(grid[0]) 
       minutes = 0
       queue = collections.deque()
       fresh = 0

       directions = [[0,1],[0,-1],[1,0],[-1,0]]

       for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                fresh += 1
            if grid[i][j] == 2:
                queue.append((i,j))

       while fresh >0 and queue:
            qlen = len(queue)
            for q in range(qlen):
                r,c = queue.popleft()

                for dr,dc in directions:
                    rw, cl = r + dr , c + dc
                    if( rw in range(row) and cl in range(col) and grid[rw][cl]==1):
                        grid[rw][cl] = 2
                        queue.append((rw,cl))
                        fresh -=1
            minutes +=1

       return minutes if fresh == 0 else -1                   
       