class Solution:
    def toLowerCase(self, s: str) -> str:
        newstr=''
        for i in s:
            newstr+=i.lower()
        return newstr
        
