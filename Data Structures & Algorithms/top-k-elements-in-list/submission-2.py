class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        heap = []

        for num in d:
            if len(heap) < k:
                heapq.heappush(heap, (d[num], num))
            else:
                heapq.heappushpop(heap, (d[num], num))
        
        return [t[1] for t in heap]