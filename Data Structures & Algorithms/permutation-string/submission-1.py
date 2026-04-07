class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_d = Counter(s1)

        s2_d = {}

        left = 0
        right = 0

        while(right < len(s2)):

            s2_d[s2[right]] = s2_d.get(s2[right], 0) + 1
            
            if right - left + 1 > len(s1):
                if s2_d[s2[left]] == 1:
                    del s2_d[s2[left]]
                else:    
                    s2_d[s2[left]] = s2_d[s2[left]] - 1
                left += 1
            if s2_d == s1_d:
                return True
            right += 1
        
        return False


