'''
Create a function called calc_dollars. In the function body, 
define a dictionary and store it in a variable named piggyBank. 
The dictionary should have the following keys defined.

quarters
nickels
dimes
pennies
For each coin type, give yourself as many as you like.

Once you have given yourself a large stash of coins in your piggybank, 
look at each key and perform the appropriate math on the integer value 
to determine how much money you have in dollars. 
Store that value in a variable named dollarAmount and print it.

Given the coins shown above, the output would be 7.07 when you call calc_dollars()
'''

def calc_dollars():
    piggy_bank = {
        "pennies": 1,
        "nickels": 1,
        "dimes": 1,
        "quarters": 1,
        "half-dollars": 1,
    }
    dollar_amount = 0

    dollar_amount += piggy_bank["pennies"] / 100
    print(dollar_amount)
    dollar_amount += piggy_bank["nickels"] / 20
    print(dollar_amount)
    dollar_amount += piggy_bank["dimes"] / 10
    print(dollar_amount)
    dollar_amount += piggy_bank["quarters"] / 4
    print(dollar_amount)
    dollar_amount += piggy_bank["half-dollars"] / 2
    print(dollar_amount)

calc_dollars()