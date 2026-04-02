class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_list = []
        res = []
        d = {}

        for s in strs:
            sorted_string = ''.join(sorted(s))
            sorted_list.append(sorted_string)
        
        
        for i in range(len(sorted_list)):
            curr = sorted_list[i]
            if curr in d:
                new_list = d[curr] 
                new_list.append(i)

                d[curr] = new_list
            else:
                d[curr] = [i]
        
        for key in d:
            values = d[key]

            curr = []
            for val in values:
                curr.append(strs[val])
            res.append(curr)


        return res