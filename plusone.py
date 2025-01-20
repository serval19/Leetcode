class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=""
        for i in digits:
            result=result+str(i)
        result2=int(result)+1
        result3=str(result2)
        arr=[]
        for i in result3:
            arr.append(int(i))
        return arr

        