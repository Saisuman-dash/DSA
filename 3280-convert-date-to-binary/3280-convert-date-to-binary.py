class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr=date.split('-')
        for i in range(len(arr)):
            arr[i]=bin(int(arr[i]))[2:]
        return arr[0]+'-'+arr[1]+'-'+arr[2]
        