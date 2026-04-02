class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while(i < len(word) and j < len(abbr)):
            if(word[i] == abbr[j]):
                i += 1
                j += 1
            elif(abbr[j].isalpha() or abbr[j] == "0"):
                return False
            else:
                sublen = 0
                while(j < len(abbr) and abbr[j].isdigit()):
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
        
        return i == len(word) and j == len(abbr)