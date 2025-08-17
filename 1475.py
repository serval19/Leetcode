class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(prices)
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    answer[i]=prices[i]-prices[j]
                    break
                else:
                    answer[i]=prices[i]
        answer[len(prices)-1]=prices[len(prices)-1]
                    
        return answer
