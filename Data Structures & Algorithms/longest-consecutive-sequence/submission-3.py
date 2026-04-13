class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nset = sorted(set(nums))
        con = 1
        res = 1

        for i in range(len(nset) - 1):
            if nset[i+1] - nset[i] == 1:
                con += 1
            else:
                res = max(res, con)
                con = 1   # reset correctly

        return max(res, con)