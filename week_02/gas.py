'''
    File name: gas.py
    Author: Victor Ramirez
    Date created: 09/05/2021
    Date last modified: 09/05/2021
    Python Version: 3.8
'''

'''
    ### 2-2. Gas Pump Informer (20 points)

    Write a script that prompts the user for a **number** of gallons of gasoline. 
    Reprint that value, along with its conversion to other measurements:

    - Equivalent number of liters (format to 4 decimals)
    - Number of barrels of oil required to produce it (format to 3 decimals)
    - Price in U.S. dollars (format to 2 decimals)

    Figures to use:

    - 1 gallon is equivalent to 3.7854 liters.
    - 1 barrel of oil produces 19.5 gallons of gas.
    - The average price of gas is approximately $3.65 per gallon.

    Save your script as: gas.py
'''
######################################################################################################
# function to convert units 
def conversion(num):    
    liter_converion = 3.7854
    num_barrels = 19.5
    ave_gallon = 3.65
        
    # convert gallons to liters
    liters = num * liter_converion
    
    # format the amounts to required decinal places
    format_liters = "{:.4f}".format(liters)    
    print('Equivalent number of liters (format to 4 decimals): ' + format_liters)    
    
    # num of barrels
    barrels = num / num_barrels
    # format the amounts to required decinal places
    format_barrels = "{:.3f}".format(barrels)
    print('Number of barrels of oil required to produce it (format to 3 decimals): ' + format_barrels)
    
    # ave price of gallon of gas
    price = ave_gallon * num
    # format the amounts to required decinal places
    format_price = "{:.2f}".format(price)
    print('Price in U.S. dollars (format to 2 decimals): $' + format_price)
######################################################################################################
    
# save user input
user_input = input("Enter the number of gallons of gasoline: ")
# enhancement TODO add user input validation

value = float(user_input)

print (user_input + ' of gallon of gas will generate the following equivalents: ')

conversion(value)
