class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        x=abs(nums[0])
        for i in nums:
            if abs(i)<x:
                x=abs(i)
        return x