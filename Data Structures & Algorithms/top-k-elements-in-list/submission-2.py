class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        #     # get freq

        # heap = []
        # for num in count.keys():
        #     heapq.heappush( heap, (count[num],num)) 
        #     if len(heap) > k :
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])

        # return res     

        count = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        res = []
        for num, freq in count.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res    



                 
     

