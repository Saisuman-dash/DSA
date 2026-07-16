class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete=arr[0]
        onedelete=arr[0]
        ansno=arr[0]
        ansone=arr[0]
        n=len(arr)
        for i in range (1,n):
            prevnodelete=nodelete
            v1=arr[i]+nodelete
            v2=arr[i]
            nodelete=max(v1,v2)
            ansno=max(nodelete,ansno)

            f1=onedelete+arr[i]
            f2=prevnodelete
            onedelete=max(f1,f2)
            ansone=max(ansone,onedelete)
        return max(ansone,ansno)