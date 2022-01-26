class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        current_price=prices[0]
        for price in prices:
            current_price=min(price,current_price)
            current_profit=price-current_price
            max_profit=max(max_profit,current_profit)
        
        return max_profit
                
        
