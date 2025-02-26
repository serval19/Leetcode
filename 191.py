class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        z=x[2:]
        count=0
        for i in z:
            if i=='1':
                count+=1
        return count
        
