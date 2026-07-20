class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0]*len(nums)
        x=0
        y=n
        for i in range (len(nums)):
            if i%2==0  :
                ans[i]=nums[x]
                x+=1
            elif i%2 !=0:
                ans[i]=nums[y]
                y+=1
        return ans
