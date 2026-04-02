class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        bucket = [[] for _ in range(n + 1)]
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Fill buckets
        for num, freq in count.items():
            bucket[freq].append(num)

        # Collect top k
        res = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
