class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        i=1
        
        while sum<=n:
            if sum<=n:
                sum+=i
            
            
            if sum==n:
                return i
                
            if sum>n:
                return i-1
            i+=1

        
