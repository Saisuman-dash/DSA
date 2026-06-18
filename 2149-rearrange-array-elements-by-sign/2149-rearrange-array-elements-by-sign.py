class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ne , p =0,0
        pos = []
        neg = []
        listi = []
        for i in range(0,n):
            if(nums[i]>=0):
                pos.append(nums[i])
            elif(nums[i]<0):
                neg.append(nums[i])
        for i in range (0,n/2):
            listi.append(pos[i])
            
            listi.append(neg[i]) 
        return listi        

        