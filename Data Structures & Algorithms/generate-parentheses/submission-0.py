class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(o: int, c: int, path):
            if(o == c and len(path) == 2*n):
                res.append(path)
                return

            if o < n:
                backtrack(o + 1, c, path + "(")

            if c < o:
                backtrack(o, c + 1, path + ")")

        backtrack(0, 0, "")
        return res