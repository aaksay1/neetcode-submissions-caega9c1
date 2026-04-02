class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        s_d = {}
        t_d = {}

        for c in s:
            if c in s_d:
                s_d[c] = s_d[c] + 1
            else:
                s_d[c] = 1
        
        for c in t:
            if c in t_d:
                t_d[c] = t_d[c] + 1
            else:
                t_d[c] = 1
    
        
        return t_d == s_d