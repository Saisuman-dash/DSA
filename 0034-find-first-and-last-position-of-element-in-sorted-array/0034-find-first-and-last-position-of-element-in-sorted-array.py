class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low =0
        high=len(nums)-1
        first=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        low =0
        high=len(nums)-1
        last=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        return [first,last]
        


    














        # first=-1
        # last=-1
        # for i in range (len(nums)):
        #     if nums[i]==target and first==-1:
        #         first=i
            
        #     if nums[i]==target and i!=first:
        #         last=i
           
        # if first!=-1 and last!=-1:
        #     return [first,last]
        # elif first==-1:
        #     return [first,last]
        # elif first!=-1 and last==-1:
        #     return [first,first]
        