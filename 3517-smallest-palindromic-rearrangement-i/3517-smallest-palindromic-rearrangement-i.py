class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        # freq={}
        left=""
        mid=None
        # right=""
        # s=sorted(s)
        # for ch in s:
        #     freq[ch]=freq.get(ch,0)+1
        # for k,v in freq.items():
        #     if freq[k]%2==0:
        #         for i in range (freq[k]//2):
        #             left+=k
        #     elif freq[k]%2!=0:
        #         for i in range (freq[k]//2):
        #             left+=k
        #         mid=k
        # right=left[::-1]
        # if len(s)%2==0:
        #     return left+right
        # else:
        #     return left+mid+right

        arr=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            arr[idx]+=1
        for i in range (26):
            ch=chr(ord('a')+i)
            if arr[i]%2==0:
                left+=ch*(arr[i]//2)
            else:
                left+=ch*(arr[i]//2)
                mid=ch
        if mid is None:
            return left+left[::-1]
        return left+mid+left[::-1]
             