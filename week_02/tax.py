'''
    File name: tax.py
    Author: Victor Ramirez
    Date created: 09/05/2021
    Date last modified: 09/05/2021
    Python Version: 3.8
'''

'''
    ### 2-4. Income Tax (20 points)

    The mythical island nation of Laskoatu has a rather simple tax code.  The first 1000 
    dollars of income is taxed at 5%.  The next 1000 dollars is taxed at 10%.  Any income 
    beyond the first 2000 dollars is taxed at 15%.  Complete the following script so that 
    it asks the user for his or her income (a **number**) and outputs the amount of tax owed.
    Format numbers to 2 decimal places.

    Example:
    ```
    Please enter your income: 1500

    The tax owed is: $100.00 
    ```

    Save your script as: tax.py
'''

# save user input
user_input = input("Please enter your income: ")
user_input_float = float(user_input)
incometax = 0.0

# calculate tax
if (user_input_float <= 1000.0):
    incometax = user_input_float * .05
elif (user_input_float > 1000.00 and user_input_float <= 2000.00):
    incometax = user_input_float * .10
else:
    incometax = user_input_float * .15

# format the dollar amounts to required decinal places
format_incometax = "{:.2f}".format(incometax)

print("The tax owed is: $ " + str(format_incometax))
