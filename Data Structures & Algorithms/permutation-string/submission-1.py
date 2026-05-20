class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)

        if ls1>ls2:
            return False

        c1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        if c1 == window:
            return True

        l=0    

        for r in range(len(s1),len(s2)):
            window[s2[r]] +=1
            window[s2[l]]  -=1   

            if window[s2[l]] == 0:
                del window[s2[l]]

            l+=1    

            if window == c1:
                return True


        return False    


