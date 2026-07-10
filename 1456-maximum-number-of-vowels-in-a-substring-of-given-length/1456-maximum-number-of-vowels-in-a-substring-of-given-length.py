class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelcount=0
        left=0
        right=0
        maxi =0
        vowels={'a', 'e', 'i', 'o', 'u'}
        for right in range (len(s)):
            if s[right] in vowels:
                vowelcount+=1
            if right-left+1>k:
                if s[left] in vowels:
                    vowelcount-=1
                left+=1
            if right-left+1 == k:
                maxi=max(maxi,vowelcount)
        return maxi
            
       