class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        res = 0

        for i in range(len(s)):

            while s[i] in q:
                q.popleft()
            q.append(s[i])
            res = max(len(q), res)
        
        return res