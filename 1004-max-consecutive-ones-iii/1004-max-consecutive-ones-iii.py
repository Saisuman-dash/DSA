class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        self.left=0
        self.right=0
        self.nums=nums
        self.k=k
        self.n=len(self.nums)
        self.maxi=0
        zeros=0

        while self.right<self.n:
            if self.nums[self.right]==0:
                zeros+=1
            while zeros>self.k:
                if self.nums[self.left]==0:
                    zeros-=1
                self.left+=1
            if zeros<=self.k:
                self.maxi=max(self.maxi,self.right-self.left+1)
            self.right+=1
        return self.maxi
