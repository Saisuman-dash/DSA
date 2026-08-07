class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        i=0
        maxi=0
        count=0
        for right in range(len(s)):
            ch=s[right]
            if ch not in freq:
                freq[ch]=freq.get(ch,0)+1
            else:
                freq[ch]+=1
            while freq[ch]>1:
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
            maxi=max(maxi,right-i+1)
        return maxi
            
                


            
