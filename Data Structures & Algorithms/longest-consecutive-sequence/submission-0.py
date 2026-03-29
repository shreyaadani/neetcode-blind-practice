class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res =0

        for num in nums:
            check, curr= 0,num
            while curr in numset:
                check+=1
                curr+=1
            res= max(res,check)

        return res                