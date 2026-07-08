class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.count =0
        self.maxi=1
        self.s=s
        self.n=len(self.s)
        self.lst=set()
        if not self.n:
            return 0
        for i in range(0,self.n):
            j = i
            while j<self.n and self.s[j] not in self.lst:
                self.lst.add(self.s[j])
                j+=1
            self.count = len(self.lst)
            self.maxi = max(self.count,self.maxi)
            self.lst.clear()
        return self.maxi

        # for i in self.s:
        #     if i in self.freq:
        #         self.count=0
        #         for k in self.freq:
        #             self.freq[k]=0
        #     self.freq[i]=self.freq.get(i,0)+1
        #     self.count+=1
        #     self.maxi=max(self.maxi,self.count)
        # return self.maxi
        # for i in range(0,self.n-1):
        #     j = i+1
        #     while j<self.n and self.s[j]!=self.s[i] : 
        #         self.count= j-i+1
        #         self.maxi=max(self.maxi,self.count)
        #         j+=1
        #     self.count = 0
        # return self.maxi

     

        