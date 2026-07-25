class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        start1,start2,end1,end2,i=0,0,0,0,0
        listu=[[intervals[0][0],intervals[0][1]]]
        j=1
        while j<len(intervals):
            start1=listu[-1][0]
            end1=listu[-1][1]
            start2=intervals[j][0]
            end2=intervals[j][1]
            if end1>=start2:
                listu[-1][0]=min(start1,start2)
                listu[-1][1]=max(end1,end2)
            else:
                listu.append([start2,end2])
            j+=1
        return listu
