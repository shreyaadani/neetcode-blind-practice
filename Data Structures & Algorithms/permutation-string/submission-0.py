class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)

        if ls1>ls2:
            return False

        for i in range(0,ls2-ls1+1):
            if Counter(s2[i:i+ls1]) == Counter(s1):
                return True

        return False        
        