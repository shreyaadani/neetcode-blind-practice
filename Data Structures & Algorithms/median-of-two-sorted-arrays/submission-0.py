class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        merge = nums1 + nums2 
        merge.sort()

        m = len(merge)
        if m % 2 ==0:
            return (merge[m // 2 - 1] + merge[m // 2] ) / 2.0
        else:
            return merge[m // 2]    