class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temparr=sorted(set(arr))
        rank={}
        for i in range (0,len(temparr)):
            rank[temparr[i]]=i+1
        for i in range (0,len(arr)):
            arr[i]=rank[arr[i]]
        return arr
        

        
        