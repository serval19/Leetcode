class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr=date.split("-")
        ans=""
        for i in arr:
            num=int(i)
            ans=ans+bin(num).replace("0b","")+"-"
        finalans=ans[:-1]
        return finalans
        
