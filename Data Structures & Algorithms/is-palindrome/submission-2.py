class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = []

        for c in s:
            if c.isalnum():
                filtered.append(c)

        l,r = 0,len(filtered)-1
        while l<r:
            if filtered[l] != filtered[r]:
                return False
            l+=1
            r-=1

        return True        

        
        