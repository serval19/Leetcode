class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n1=bin(x)[2:]
        n2=bin(y)[2:]
        num1=list(n1)
        num2=list(n2)
        width=max(len(n1),len(n2))
        num1 = (['0'] * (width - len(num1))) + num1  # Fixed
        num2 = (['0'] * (width - len(num2))) + num2  # Fixed
        ans=0
        for i in range(width):
            if num1[i]!=num2[i]:
                ans+=1
        return ans
        
