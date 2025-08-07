class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum1=0
        for i in range(1,num):
            if num%i==0:
                sum1+=i
        if sum1==num:
            return True
        else:
            return False
# memory limit exceeded error
