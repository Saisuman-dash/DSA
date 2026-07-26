class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # found=False
        first=-1
        last=-1
        for i in range (len(nums)):
            if nums[i]==target and first==-1:
                first=i
                # found=True
            if nums[i]==target and i!=first:
                last=i
                # found=True
        # if found==False:
        #     return [-1,-1]
        if first!=-1 and last!=-1:
            return [first,last]
        elif first==-1:
            return [first,last]
        elif first!=-1 and last==-1:
            return [first,first]
        