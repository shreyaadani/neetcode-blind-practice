class WordDictionary:

    def __init__(self):
        self.dic ={}


        

    def addWord(self, word: str) -> None:
        level = self.dic
        word+='#'
        for c in word:
            if c not in level:
                level[c] = {}
            level = level[c]    




    def search(self, word: str) -> bool:
        word += '#'
        
    
        def dfs(level, i):
            if i == len(word):
                return True
            
            c = word[i]
            
            if c == '.':
                for child in level:
                    if dfs(level[child], i + 1):
                        return True
                return False
           
            else:
                
                    if c in level:
                         return dfs(level[c],i + 1)
                    else:
                        return False    
            
                
        
        return dfs(self.dic, 0)


        
