class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob,norob=0,0
        for num in nums:
            newrob=norob+num
            newnorob=max(norob,rob)
            rob,norob=newrob,newnorob
        return max(rob,norob)
        
