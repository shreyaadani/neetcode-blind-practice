class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,best =0,0
        freq={}
        maxfreq = 0

        for r in range(0,len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxfreq = max(maxfreq,freq[s[r]])
            while r-l+1 - maxfreq > k:
                freq[s[l]]-=1
                l+=1
            best = max(best,r-l+1)

        return best        
        