class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0]*len(nums)
        x=nums[:n]
        y=nums[n:]
        px=0
        py=0

        for i in range (len(nums)):
            if i%2==0 :
                ans[i]=x[px]
                px+=1
            elif i%2 !=0:
                ans[i]=y[py]
                py+=1
        return ans
