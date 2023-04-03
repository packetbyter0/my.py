# Author: Quintin Schroeer
# Date: 16.03.2023

my_budget=21450.00
print(f"My budget for trading stocks is {my_budget}€")
share_appl_name="Apple Inc. (AAPL)"
share_value_aapl_last_week=67.61
max_quantity_of_shares_aapl=int(my_budget/share_value_aapl_last_week)
print(f"A maximum of {max_quantity_of_shares_aapl} shares of Apple Inc. (AAPL) can be bought.")
number_of_shares_aapl_bought=150
remaining_budget=my_budget-((max_quantity_of_shares_aapl-number_of_shares_aapl_bought)*share_value_aapl_last_week)
print(f"After buying stock {max_quantity_of_shares_aapl-number_of_shares_aapl_bought}, the remaining budget is {remaining_budget}€")
share_value_aapl_tuday=65.98
my_budget=remaining_budget+((max_quantity_of_shares_aapl-number_of_shares_aapl_bought)*share_value_aapl_tuday)
print(f"If I were to sell my shares Apple Inc. (AAPL) today, I would make a loss of {my_budget-(my_budget-(max_quantity_of_shares_aapl-number_of_shares_aapl_bought)*share_value_aapl_tuday+(max_quantity_of_shares_aapl-number_of_shares_aapl_bought)*share_value_aapl_last_week)} and my available budget would be {my_budget}€")
