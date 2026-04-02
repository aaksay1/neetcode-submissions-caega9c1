class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha(): # is a letter
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:  # number in abbr
                if abbr[j] == '0':  # leading zero is invalid
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num  # skip 'num' letters in word

        return i == len(word) and j == len(abbr)





