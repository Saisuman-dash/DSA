class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1,index2=-1,-1
        i=0
        j=len(numbers)-1
        while i<j:
            sumi=numbers[i]+numbers[j]
            if sumi>target:
                j-=1
            elif sumi<target:
                i+=1
            elif sumi==target:
                return [i+1,j+1]