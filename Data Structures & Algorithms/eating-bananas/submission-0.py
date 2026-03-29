class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k:int)-> bool:
            total = sum(((p+k-1) // k) for p in piles)
            return total <= h    
        
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if canfinish(mid):
                high = mid
            else:
                low = mid + 1

        return low