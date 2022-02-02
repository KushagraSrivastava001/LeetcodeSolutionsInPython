class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=set()
        for key in d.keys():
            s.add(d[key])
        return len(s)==1
