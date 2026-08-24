class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #    prod, zero_cnt = 1,0
    #    for num in nums:
    #     if num:
    #         prod*=num #nonzero
    #     else:
    #         zero_cnt += 1

    #    if zero_cnt >1:
    #     return [0]*len(nums) #allzero   


    #    res= [0]*len(nums)
    #    for i, c in enumerate(nums):
    #     if zero_cnt:
    #         res[i] = 0 if c else prod

    #     else:
    #         res[i] = prod//c
    #    return res     

        left = [1]*len(nums)
        right = [1]*len(nums)
        res = [1]*len(nums)
        n = len(nums)
        left[0] = 1
        right[n-1] = 1

        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right[i]= right[i+1]*nums[i+1]

        for i in range(len(nums)):
            res[i] = left[i]*right[i]    

        return res    
        
