class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        heap = []

        for num, freq in d.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        
        return [t[1] for t in heap]