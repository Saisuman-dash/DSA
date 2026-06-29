class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq ={}
        freqq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in t:
            freqq[i]=freqq.get(i,0)+1
        if freq == freqq :
            return True
        else:
            return False