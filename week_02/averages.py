'''
    File name: averages.py
    Author: Victor Ramirez
    Date created: 09/05/2021
    Date last modified: 09/05/2021
    Python Version: 3.8
'''

'''
    ### 2-3. Number Averager (20 points)

    Write a script that prompts the user for **two numbers**, a and b. 
    Then, prompt the user to enter a type of average out of the three options below. 
    Make it so the user would just type in a **number** 1, 2 or 3 for the 
    average (i.e. 1 for arithmetic mean, 2 for geometric mean, or 3 for root-mean-square). 
    This numerical selection is an example of how to give the user a simple response that will 
    get around potential spelling errors and head off user frustration. This design decision 
    makes the user interaction more robust. No requirement to round or format numbers for this 
    problem. Output the correct average, based on what the user selected.

    1. The arithmetic mean:  $(a + b) / 2 $
    2. The geometric mean:  $\sqrt{ab}$
    3. The root-mean-square: $\sqrt{\frac{a^2 + b^2}{2}}$

    Save your script as: averages.py

'''

import math

# save user input
first_number_user_input = input("Enter two numbers. Please enter the first number: ")
second_number_user_input = input("Please enter the second number: ")
print("Please select the type of average out of the three options below.: ")
print("")
print("1. The arithmetic mean:  (a + b) / 2 ")                                        
print("2. The geometric mean:  square root of (ab)")
print("3. The root-mean-square: square root of (a^2 + b^2) / 2")
print("")
ave_user_input = input("Please enter the type of average to calculate: ")
# enhancement TODO add user input validation

num1_float = float(first_number_user_input)
num2_float = float(second_number_user_input)
result = 0.0

if (ave_user_input == '1'):
    # arithmetic_mean = (num1_float + num2_float) / 2.0
    result = (num1_float + num2_float) / 2.0
elif (ave_user_input == '2'):
    # geometric_mean = math.sqrt(num1_float * num2_float)
    result = math.sqrt(num1_float * num2_float)    
elif (ave_user_input == '3') :
    # root_mean_square = math.sqrt(((num1_float ** 2 ) + (num2_float ** 2 )) / 2 )
    result = math.sqrt(((num1_float ** 2 ) + (num2_float ** 2 )) / 2 )

print('The average calculated is: ' + str(result))
