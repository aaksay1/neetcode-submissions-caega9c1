class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)

        i = 0
        j = 0

        while(i < n and j < m):
            if(word[i] == abbr[j]):
                i += 1
                j += 1
            elif(abbr[j].isalpha() or abbr[j] == "0"):
                return False
            else:
                sublen = 0
                while(j < m and abbr[j].isdigit()):
                    sublen = sublen * 10 + int(abbr[j])
                    j+=1
                i += sublen

        return i == n and j == m