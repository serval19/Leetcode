class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        numtrees=[1]*(n+1)
        for nodes in range(2,n+1):
            total=0
            for root in range(1,nodes+1):
                left=root-1
                right=nodes-root
                total+=numtrees[left]*numtrees[right]
            numtrees[nodes]=total
        return numtrees[n]


        
