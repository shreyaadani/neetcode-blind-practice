class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # col = len(grid[0])
        # row = len(grid)
        # res = 0


        # def dfs(i,j):
        #     if i<0 or j<0 or i>=row or j >= col or grid[i][j]=="0":
        #         return 

        #     grid[i][j] = "0"
        #     dfs(i+1,j)
        #     dfs(i,j+1)
        #     dfs(i-1,j)
        #     dfs(i,j-1)

        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == "1":
        #             dfs(i,j)
        #             res+= 1

        # return res                    

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def bfs(i,j):
            q = deque()
            grid[i][j]= "0"
            q.append((i,j))
            while q:
                row , col = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+row , dc+col
                    if nc<0 or nr<0 or nr>=rows or nc>=cols or grid[nr][nc] =="0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"    



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1

        return res            
