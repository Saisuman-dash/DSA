class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = set()
        maxi = 0
        n = len(s)
        for right in range (0,n):
            
            while s[right] in freq:
                
                freq.remove(s[left])
                left += 1
            maxi = max(maxi,right-left+1)
            freq.add(s[right])
        return maxi

            
        