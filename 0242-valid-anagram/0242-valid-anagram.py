class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        val=0
        if len(t)<len(s):
            return False
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if ch not in freq:
                return False
            freq[ch]-=1
            val=freq[ch]
            if val==-1:
                return False
        return True
        