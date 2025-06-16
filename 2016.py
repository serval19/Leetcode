class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maxdiff=-1
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    diff=nums[j]-nums[i]
                    if diff>maxdiff:
                        maxdiff=diff
        return maxdiff

        
