class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh,sm,ss=map(int,startTime.split(":"))
        eh,em,es=map(int,endTime.split(":"))
        stsec=3600*sh + 60*sm + ss
        ensec= (3600*eh)+(60*em)+es
        return ensec-stsec