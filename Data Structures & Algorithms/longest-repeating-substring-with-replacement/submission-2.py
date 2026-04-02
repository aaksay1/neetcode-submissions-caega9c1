class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        max_freq = 0
        res = 0

        left = 0

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = d[s[i]] + 1
            else:
                d[s[i]] = 1
            
            max_freq = max(max_freq, d[s[i]])

            while((i - left + 1) - max_freq > k):
                d[s[left]] = d[s[left]] - 1
                left += 1
            
            res = max(res, i - left + 1)

        return res