class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
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
        for i in range (0,int(n/2)):
            listi.append(pos[i])
            listi.append(neg[i]) 
        return listi    