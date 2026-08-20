class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[]
        arr2=[]
        val=0
        for i in range (len(nums)):
            if i>1:
                val=max(arr1[-1],arr2[-1])
                if val==arr1[-1]:
                    arr1.append(nums[i])
                if val==arr2[-1]:
                    arr2.append(nums[i])
            if i==0:
                arr1.append(nums[i])
            elif i==1:
                arr2.append(nums[i])
        return arr1+arr2
