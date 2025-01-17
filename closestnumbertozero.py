class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        x=nums[0]
        for i in nums:
            if abs(i)<abs(x):
                x=i
        if x<0 and abs(x) in nums:
            return abs(x)
        return x
            