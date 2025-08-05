# need to optimize this code since it will show time limit exceeded error in leetcode
class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        
        testnum=n-1
        isprime=False
        ispalindrome=False
        if n==1:
            return 2
        
        
        while  not(isprime and ispalindrome):
            testnum+=1
            string=str(testnum)
            
            
            if string==string[::-1]:
                ispalindrome=True
            else:
                ispalindrome=False
            for i in range(2,int(sqrt(testnum)+1)):
                if testnum%i==0:
                    isprime=False
                    break
            else:
                isprime=True
        return testnum
            

        
            
