class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for char in strs:
            key =''.join(sorted(list(char)))
            if key not in d:
                d[key]=[char]
            else:
                d[key].append(char)
        
        return sorted(list(d.values()))
        
