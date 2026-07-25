class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        tof=0
        for i in range (len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for k,v in freq.items():
            if freq[k]==1:
                tof=k
                break
        for i in range (len(s)):
            if s[i]==tof:
                return i
                break
        return -1
