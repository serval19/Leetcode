class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binnum=bin(n)[2:]
        for i in range(len(binnum)-1):
            if binnum[i]==binnum[i+1]:
                return False
        return True