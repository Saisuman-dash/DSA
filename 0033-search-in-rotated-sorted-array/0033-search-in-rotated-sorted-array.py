class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
        # newv=-1
        # oldv=-1
        # # if target not in nums :
        # #     return -14
        # for i in range (len(nums)):
        #     if nums[i]==target:
        #         oldv=i
        #         break
        # if oldv==-1:
        #     return -1
        # ans=sorted(nums)
        # for i in range (len(ans)):
        #     if ans[i]==target:
        #         newv=i
        #         break
        
        # print(oldv)
        # print(newv)
        # if oldv==newv:
        #     return oldv
        # else:
        #     return oldv-newv
        
    

        