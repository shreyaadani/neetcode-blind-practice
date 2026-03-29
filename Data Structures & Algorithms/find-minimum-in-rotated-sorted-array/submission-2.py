class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n//2
        res = nums[mid]
        for i in range(n):
            if nums[i]< nums[mid]:
                res= min(nums[i],res)
            else:
                mid = i

        return res            

    

        