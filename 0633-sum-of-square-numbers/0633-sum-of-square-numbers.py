class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums=[0]*(int(sqrt(c))+1)
        print(int(sqrt(c)))
        for i in range (int(sqrt(c))+1):
            nums[i]=(i)**2
            if nums[i]==c:
                return True
            
        left=0
        right=len(nums)-1
        while left<=right:
            sum=nums[left]+nums[right]
            if sum>c:
                right-=1
            if sum<c:
                left+=1
            if sum==c:
                return True
        return False
        

        