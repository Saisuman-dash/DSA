class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f=len(firstList)
        s=len(secondList)
        minu=min(f,s)
        start1=0
        start2=0
        end1=0
        end2=0
        anslist=[]
        i=0
        j=0
        if minu==0:
            return []
        while i!=len(firstList) and j!= len(secondList):
            start1=firstList[i][0]
            start2=secondList[j][0]
            end1=firstList[i][1]
            end2=secondList[j][1]
            start=max(start1,start2)
            end=min(end1,end2)
            if start<=end:
                anslist.append([start,end])
            if end==end1:
                i+=1
            else:
                j+=1
            
        return anslist
        