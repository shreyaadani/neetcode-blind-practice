class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.reccur(i,j,0,board,word,set()):
                        return True    

            return False


    def reccur(self,i,j,c,board,word,visit):

        if c >= len(word):
            return True
        if i >= len(board) or j>= len(board[0]) or i< 0 or j <0:
            return False

        if (i,j) in visit:
            return False   
            

        res = False
        if board[i][j] == word[c]:
            visit.add((i,j))
            res= res or  self.reccur(i,j+1,c+1,board,word,visit.copy())
            res= res or  self.reccur(i+1,j,c+1,board,word,visit.copy())
            res= res or self.reccur(i-1,j,c+1,board,word,visit.copy())
            res= res or  self.reccur(i,j-1,c+1,board,word,visit.copy()) 

        return res   




        