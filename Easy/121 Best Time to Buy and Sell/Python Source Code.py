class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lu = list()

        while prices.index(max(prices)) == 0:
            
            prices.pop(0)

        for i in range(0 , prices.index(max(prices))):
            
            lu.append(max(prices) - prices[i])
            
        if len(lu) != 0: 
            
            maxi = max(lu)
        
        else :
            
            maxi = 0

        for _ in sample_array:

            if len(prices) == 0:
                
                return 0
            
            elif prices.index(max(prices)) < prices.index(min(prices)):
                
                prices.pop(prices.index(max(prices)))
                count += 1

            else:
                
                if max(prices) - min(prices) >= maxi:
                    
                    return max(prices) - min(prices)

                else :
                    
                    return maxi
