from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return -1
        
        total_customers = 0
        
        profits = []

        i = 1
        
        total_customers += customers[0]

        while total_customers > 0 or i < len(customers):
            if total_customers >= 4:
                current_customers = 4
                total_customers -= 4
            else:
                current_customers = total_customers
                total_customers = 0
            current_profit = current_customers * boardingCost - runningCost
            profits.append(current_profit)
            if i < len(customers):
                total_customers += customers[i]
                i += 1
        
        for i in range(1, len(profits)):
            profits[i] += profits[i - 1]
        max_profit = max(profits)
        index = profits.index(max_profit)
        if max_profit <= 0:
            return -1
        else:
            return index + 1

            
