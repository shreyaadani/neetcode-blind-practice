class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapn = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapn:
                return[mapn[comp],i]
            else:
                mapn[nums[i]] = i

        return []            