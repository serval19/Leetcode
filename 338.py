class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(0,n+1):
            binary=bin(i)[2:]
            count=binary.count('1')
            arr.append(count)
        return arr
