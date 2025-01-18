class Solution:
    def myPow(self, x: float, n: int) -> float:
        result=1
        for i in range(abs(n):
            result=result*x
        if n>0:
            return result
        elif n<0:
            result=1.0/result
            return result
        else:
            return 1
        