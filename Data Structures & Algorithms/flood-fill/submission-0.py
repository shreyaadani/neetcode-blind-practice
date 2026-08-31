class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        row = len(image)
        col = len(image[0])

        if original == color:
            return image

        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or image[i][j]!= original:
                return 
            image[i][j] = color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(row):
            for j in range(col):
                if image[i][j] == original:
                    dfs(sr,sc)

        return image            
