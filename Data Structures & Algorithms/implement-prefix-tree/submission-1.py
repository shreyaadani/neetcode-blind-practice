class PrefixTree:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        level=self.dic
        word+="#"
        for c in word:
            if c not in level:
                level[c]={}
            level=level[c]
            



    def search(self, word: str) -> bool:
        level = self.dic
        word+="#"
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        level = self.dic
        for c in prefix:
            if c in level:
                level = level[c]  
            else:
                return False
        return True
        
        