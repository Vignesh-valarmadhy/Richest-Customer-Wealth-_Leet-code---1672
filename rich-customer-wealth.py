from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize max_wealth to store the maximum wealth found
        max_wealth = 0

        # Iterate through each customer's account
        for customer_account in accounts:
            # Calculate the wealth of the current customer
            current_wealth = sum(customer_account)

            # Update max_wealth if the current customer's wealth is greater
            max_wealth = max(max_wealth, current_wealth)

        # Return the maximum wealth found
        return max_wealth


solution_instance = Solution()
accounts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = solution_instance.maximumWealth(accounts)
print("Maximum wealth:", result)
