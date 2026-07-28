class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        freq={}
        left=""
        mid=""
        right=""
        s=sorted(s)
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for k,v in freq.items():
            if freq[k]%2==0:
                for i in range (freq[k]//2):
                    left+=k
            elif freq[k]%2!=0:
                for i in range (freq[k]//2):
                    left+=k
                mid=k
        right=left[::-1]
        if len(s)%2==0:
            return left+right
        else:
            return left+mid+right
        
        