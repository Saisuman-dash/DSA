class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s = s
        self.seen = {}
        self.left=0
        self.right=0
        self.n=len(self.s)
        self.maxi=1
        self.length=0
        if not self.n:
            return 0
        while self.right<self.n:
            if self.s[self.right] in self.seen and self.seen[self.s[self.right]]>=self.left:
                self.left = self.seen[s[self.right]]+1
                self.seen[s[self.right]]=self.right



            self.maxi=max(self.maxi,self.right-self.left+1)
            self.seen[self.s[self.right]]=self.right
            self.right+=1
        return self.maxi
            

