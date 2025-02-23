class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        sum=0
        x=abs(x)
        while x!=0:
            rem=x%10
            sum=sum*10+rem
            
            x=x//10
        sum=sum*sign
        if sum<-1*(2**31) or sum>(2**31)-1:
            return 0
        return sum


        
