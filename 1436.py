class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l1=[]
        l2=[]
        for i in paths:
            l1.append(i[0])
            l2.append(i[1])
        for i in l2:
            if i not in l1:
                return i
        
